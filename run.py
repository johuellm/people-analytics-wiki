from jinja2 import Environment, FileSystemLoader
import os
from csv import DictReader
from itertools import groupby
from operator import itemgetter
from io import StringIO
import csv
import subprocess

def build_templates(): 
  # Paths
  root = os.path.dirname(os.path.abspath(__file__))
  templates_dir = os.path.join(root, 'templates')

  # Templates
  env = Environment( loader = FileSystemLoader(templates_dir) )
  table = env.get_template('table.html')
  details = env.get_template('singlePageTemplate.html')
  contentPage = env.get_template('contentPage.html')

  # Output file paths
  filename_index = os.path.join(root, 'html', 'index.html')
  filename_consultancies = os.path.join(root, 'html', 'consultancies.html')
  filename_academics = os.path.join(root, 'html', 'academics.html')
  about = os.path.join(root, 'html', 'about.html')
  helpPage = os.path.join(root, 'html', 'help.html')
  vendors_folder = os.path.join(root,"html", "vendors")

  # Load content
  aboutContent = open("templates/about.html","r").read()
  helpContent = open("templates/help.html","r").read()
  vendors_csv = csv.reader( open("csv/Vendors_Coding.csv", "r" ), delimiter=';' )
  # consultancies_csv = csv.reader(open("csv/Consultancies_Coding.csv", "r"), delimiter=';')
  # academics_csv = csv.reader(open("csv/Academics_Coding.csv", "r"), delimiter=";")

  vendors_data = [ row for row in vendors_csv]
  # consultancies_data = [row for row in consultancies_csv]
  # academics_data = [row for row in academics_csv if not "".join(row).startswith('#')]

  # create necessary folders
  if not os.path.exists(vendors_folder):
    os.makedirs(vendors_folder)

  # run the templating engine
  with open(about, 'w+') as f:
      f.write(contentPage.render(data=aboutContent))

  with open(helpPage, 'w+') as f:
      f.write(contentPage.render(data=helpContent))

  for row in vendors_data[2:]:
      singlepage = os.path.join(vendors_folder, row[1]+'.html')
      with open(singlepage, 'w+') as f:
          f.write(details.render(data=row, head=vendors_data[0], tooltip=vendors_data[1]))

  with open(filename_index, 'w+') as f:
      f.write(table.render(data=vendors_data))

  # with open(filename_consultancies, 'w+') as f:
  #     f.write(table.render(data=consultancies_data))

  # with open(filename_academics, 'w+') as f:
  #     f.write(table.render(data=academics_data))



def copy_static_files():

  # copy static files using cp, because shutil has some gimmicks with wsl (windows subsystem for linux)

  # create top-level folder
  if not os.path.exists("html"):
    os.makedirs("html")

  css_path = os.path.join("html", "css")
  if not os.path.exists(css_path):
    os.makedirs(css_path)
  subprocess.call('cp -r ./css/* %s' % css_path, shell=True)

  datatables_path = os.path.join("html", "datatables")
  if not os.path.exists(datatables_path):
    os.makedirs(datatables_path)
  subprocess.call('cp -r ./datatables/* %s' % datatables_path, shell=True)
  
  js_path = os.path.join("html", "js")
  if not os.path.exists(js_path):
    os.makedirs(js_path)
  subprocess.call('cp -r ./js/* %s' % js_path, shell=True)

  resources = os.path.join("html", "resources")
  if not os.path.exists(resources):
    os.makedirs(resources)
  subprocess.call('cp -r ./resources/* %s' % resources, shell=True)



if __name__ == "__main__":
  build_templates()
  copy_static_files()
