from pathlib import Path
#jinja packages are used to generate the html and pdf files from the data in data.py
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from data import PDC_Circuit_Strings

#Sets the base directory to the current file's parent directory
BASE_DIR = Path(__file__).parent

#Creates a Jinja2 environment with the templates directory as the loader 
# and StrictUndefined to raise an error for undefined variables
env = Environment(
    loader=FileSystemLoader(BASE_DIR.joinpath("templates")),
    undefined=StrictUndefined,
)

def build(circuits, out_name="string_sheet"):
    html = env.get_template("string_sheet.html").render(circuits=circuits)
    (BASE_DIR.joinpath(f"{out_name}.html")).write_text(html, encoding="utf-8")
    from weasyprint import HTML
    HTML(string=html).write_pdf(BASE_DIR.joinpath(f"{out_name}.pdf"))
    return html
'''
if __name__ == "__main__":
    build(PDC_Circuit_Strings)
    print("wrote sheet.html and sheet.pdf")
'''
long_circuit = {
    "circuit_number": 99,
    "circuit_name": "Page break test",
    "drawing_number": "TEST",
    "type": "Test",
    "circuit_strings": [PDC_Circuit_Strings[0]["circuit_strings"][0]] * 1000
}
build([long_circuit], "pagetest")   

