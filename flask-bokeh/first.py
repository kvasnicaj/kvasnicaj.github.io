from flask import Flask, render_template
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

# načtení dat ze souboru do pandas (TODO: nahradit za mongo)
iris_df = pd.read_csv("data/iris.data",
                      names=["Sepal Length",
                             "Sepal Width",
                             "Petal Length",
                             "Petal Width",
                             "Species"
                             ])
# seznam názvu sloupců bez posledního
feature_names = iris_df.columns[0:-1].values.tolist()


# vytvoření hlavního grafu (barevný Bokeh histogram)
def create_circle_figure(colors, fill_alpha=0.2, size=10):

    p = figure(title='Iris example')

    # Set the x axis label
    p.xaxis.axis_label = 'Petal Length'

    # Set the y axis label
    p.yaxis.axis_label = 'Petal Width'

    p.circle(iris_df['Petal Length'], iris_df['Petal Width'],
             color=colors, legend="3*sin(x)", fill_alpha=0.2, size=10)
    return p


@app.route('/')
def index():
    colormap = {'Iris-setosa': 'red', 'Iris-versicolor': 'green',
                'Iris-virginica': 'blue'}
    colors = [colormap[x] for x in iris_df['Species']]

    # Create the plot - vytvoření grafu
    plot = create_circle_figure(colors)
    plot2 = create_circle_figure(colors)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    script2, div2 = components(plot2)
    return render_template("index.html", script=script,
                           div=div, script2=script2, div2=div2)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
