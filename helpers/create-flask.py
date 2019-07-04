"""
Připraví adresářovou strukturu a základní soubory pro nový Flask projekt.

project_directory
├── config
│   ├── __init__.py
│   └── config.py
└── static
│   ├── css
│   ├── icons
│   ├── images
│   └── js
└── templates
│   ├── layouts
│   │   └── main.html
│   └── errors
├── .gitignire
├── .gitattributes
└── app.py
"""
import os
from pathlib import Path
import argparse

# definice argumentů pro příkazovou řádku
parser = argparse.ArgumentParser(
    description='Creates folder structure for Flask project')
parser.add_argument('-p', metavar='path', default=os.getcwd(),
                    help='Path to your project directory, default: cwd')
parser.add_argument('-d', metavar='description', default='New project',
                    help='Project description in meta tags')
parser.add_argument('-a', metavar='author', default='Anonymous',
                    help='Author in meta tags')
parser.add_argument('-c', metavar='charset', default='utf-8',
                    help='Charset for html file, default: utf-8')
parser.add_argument('-l', metavar='lang', default='cs',
                    help='Language for html file, default: cs')

# parsování argumentů
arguments = parser.parse_args()

# nastavení adresáře projektu
project_directory = arguments.p

# adresářová struktura
folders = ['config',
           'static/css',
           'static/js',
           'static/images',
           'static/icons',
           'templates/layouts',
           'templates/errors']

# 1. vytvoření adresářové struktury
for folder in folders:
    try:
        os.makedirs(f'{project_directory}/{folder}', exist_ok=True)
    except OSError as e:
        print(f'{project_directory} | {folder} :: {e}')

# 2. vytvoření souboru .gitignore
with open(project_directory + '/.gitignore', 'w') as f:
    f.write('__pycache__\n.DS_Store\n.vscode\n')

# 3. vytvoření souboru .gitattribuites
with open(project_directory + '/.gitattributes', 'w') as f:
    f.write('static/* linguist-vendored\n')

# 4. vytvoření konfiguračního souboru
with open(project_directory + '/config/config.py', 'w') as f:
    f.write('class Config(object):\n    DEBUG = True\n')

# 5. vytvoření __init__.py v konfiguračním adresáři
Path(project_directory + '/config/__init__.py').touch()

# 6. vytvoření layoutu
with open(project_directory + '/templates/layouts/main.html', 'w') as f:
    f.write(f'<!doctype html>\n'
            f'<html lang="{arguments.l}">\n'
            f'<head>\n'
            f'  <meta charset="{arguments.c}" >\n'
            f'  <meta name="description" content="{arguments.d}">\n'
            f'  <meta name="author" content="{arguments.a}">\n\n'
            f'  <title> {{ % block title % }}{{ % endblock % }} </title>\n'
            f'  <link rel="stylesheet" href="'
            f'https://stackpath.bootstrapcdn.com/'
            f'bootstrap/4.3.1/css/bootstrap.min.css" '
            f'integrity="'
            f'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784'
            f'j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" '
            f'crossorigin="anonymous">\n'
            f'</head>\n'
            f'<body>\n'
            f'  {{% block content %}}'
            f'  {{% endblock %}}'
            f'</body>\n'
            f'</html>'
            )

# 7. vytvoření app.py
with open(project_directory + '/app.py', 'w') as f:
    f.write(f'from flask import Flask\n'
            f'from config.config import Config\n\n'
            f'app = Flask(__name__)\n\n'
            f'configuration = Config()\n'
            f'app.config.from_object(configuration)\n\n'
            f"if __name__ == '__main__':\n"
            f'    app.run()\n'
            )
