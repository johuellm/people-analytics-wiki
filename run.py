from jinja2 import Environment, FileSystemLoader
import os
from csv import DictReader
from itertools import groupby
from operator import itemgetter
from io import StringIO
import csv

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
table = env.get_template('table.html')
details = env.get_template('singlePageTemplate.html')
contentPage = env.get_template('contentPage.html')
filename = os.path.join(root, 'html', 'index.html')
about = os.path.join(root, 'html', 'about.html')
helpPage = os.path.join(root, 'html', 'help.html')

aboutContent = open("resources/about.html","r").read()
helpContent = open("resources/help.html","r").read()

rdr= csv.reader( open("csv/Coding.csv", "r" ), delimiter=';' )
csv_data = [ row for row in rdr ]

with open(about, 'w+') as f:
    f.write(contentPage.render(data=aboutContent))

with open(helpPage, 'w+') as f:
    f.write(contentPage.render(data=helpContent))

for row in csv_data:
    singlepage = os.path.join(root, 'html', row[1]+'.html')
    with open(singlepage, 'w+') as f:
        f.write(details.render(data=row, head=csv_data[0], tooltip=csv_data[1]))

with open(filename, 'w+') as f:
    f.write(table.render(data=csv_data))

