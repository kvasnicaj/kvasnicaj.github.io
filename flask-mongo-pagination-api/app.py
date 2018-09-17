from flask import Flask, request, render_template
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/grainery'

mongo = PyMongo(app)


def paginationQuery(collection, limit, offset):
    """vrátí stanovený počet řádků (limit) a přeskočí jich o offset
    (pouze pokud je offset vyšší než nula) a celkový počet řádků """

    rows = collection.find() \
        .skip(offset if offset > 0 else 0) \
        .limit(limit) \
        .sort('_id', pymongo.ASCENDING)

    max = rows.count()

    return (rows, max)


@app.route('/numbers', methods=['GET'])
def numbers():

    collection = mongo.db.numbers
    offset = int(request.args['offset'])
    limit = int(request.args['limit'])

    numbers = paginationQuery(collection, limit, offset)
    output = []

    # projdu výsledek dotazu a výsledky dám do seznamu
    for i in numbers[0]:
        output.append({'number': i['number']})

    return render_template('numbers.html', output=output,
                           offset=offset, limit=limit, max=numbers[1])


if __name__ == '__main__':
    app.run(debug=True)
