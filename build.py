from pathlib import Path
#jinja packages are used to generate the html and pdf files from the data in data.py
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from weasyprint import HTML
from data import PDC_Circuit_Strings

#Sets the base directory to the current file's parent directory
BASE_DIR = Path(__file__).parent

#Creates a Jinja2 environment with the templates directory as the loader 
# and StrictUndefined to raise an error for undefined variables
env = Environment(
    loader=FileSystemLoader(BASE_DIR.joinpath("templates")),
    undefined=StrictUndefined,
)

#
def render_sheet(input_circuits):
    return env.get_template("string_sheet.html").render(circuits=input_circuits)

def write_pdf(html, path):
    HTML(string=html).write_pdf(path)

def write_pdf_byte(html):
    return HTML(string=html).write_pdf()

#Testing
if __name__ == "__main__":
    html = render_sheet(PDC_Circuit_Strings)
    write_pdf(html, BASE_DIR.joinpath("test_output.pdf"))
    print("wrote test_output.pdf")
