import datetime
import os
from dotenv import load_dotenv

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts import get_format_year, read_exel_file, get_dict_with_alcohol


if __name__ == '__main__':
    load_dotenv()
    xsl_filepath = os.getenv('XLS_FILEPATH', default='wine.xlsx')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    years_company = datetime.datetime.now().year - 1920
    try:
        wines = read_exel_file(xsl_filepath).to_dict(orient="records")
    except (FileNotFoundError):
        print(f"Файл: {xsl_filepath} не найден")
    alcohols = get_dict_with_alcohol(wines)

    rendered_page = template.render(
        years_company = years_company,
        conjugation_year = get_format_year(years_company),
        alcohols = alcohols,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
