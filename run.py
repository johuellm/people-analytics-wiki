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

filename = os.path.join(root, 'html', 'test.html')




rdr= csv.reader( open("csv/Coding.csv", "r" ), delimiter=';' )
csv_data = [ row for row in rdr ]
i=1
for row in csv_data:

    i = i+1
    singlepage = os.path.join(root, 'html', row[1]+'.html')
    with open(singlepage, 'w+') as f:
        f.write(details.render(data=row))

with open(filename, 'w+') as f:
    f.write(table.render(data=csv_data))

