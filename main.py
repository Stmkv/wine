import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts import get_format_year, read_exel_file

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

now = datetime.datetime.now()
years_company = now.year - 1920
wines = read_exel_file('wine.xlsx').to_dict(orient="records")


rendered_page = template.render(
    years_company = years_company,
    conjugation_year = get_format_year(years_company),
    name_wine = wines,
    wines = wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
