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
filename_index = os.path.join(root, 'html', 'index.html')
filename_consultancies = os.path.join(root, 'html', 'consultancies.html')
filename_academics = os.path.join(root, 'html', 'academics.html')
about = os.path.join(root, 'html', 'about.html')
helpPage = os.path.join(root, 'html', 'help.html')

aboutContent = open("resources/about.html","r").read()
helpContent = open("resources/help.html","r").read()

vendors_csv = csv.reader( open("csv/Coding.csv", "r" ), delimiter=';' )
consultancies_csv = csv.reader(open("csv/Consultancies_Coding.csv", "r"), delimiter=';')
academics_csv = csv.reader(open("csv/Academics_Coding.csv", "r"), delimiter=";")

vendors_data = [ row for row in vendors_csv ]
consulatncies_data = [row for row in consultancies_csv]
academics_data = [row for row in academics_csv]

with open(about, 'w+') as f:
    f.write(contentPage.render(data=aboutContent))

with open(helpPage, 'w+') as f:
    f.write(contentPage.render(data=helpContent))

for row in vendors_data:
    singlepage = os.path.join(root, 'html', row[1]+'.html')
    with open(singlepage, 'w+') as f:
        f.write(details.render(data=row, head=vendors_data[0], tooltip=vendors_data[1]))

with open(filename_index, 'w+') as f:
    f.write(table.render(data=vendors_data))

with open(filename_consultancies, 'w+') as f:
    f.write(table.render(data=consulatncies_data))

with open(filename_academics, 'w+') as f:
    f.write(table.render(data=academics_data))