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

#Builds the HTML and PDF files from the circuit data
def build_sheet(circuits, out_name="string_sheet"):
    html = env.get_template("string_sheet.html").render(circuits=circuits)
    (BASE_DIR.joinpath(f"{out_name}.html")).write_text(html, encoding="utf-8")
    from weasyprint import HTML
    HTML(string=html).write_pdf(BASE_DIR.joinpath(f"{out_name}.pdf"))
    return html


#Testing build function with the PDC_Circuit_Strings data from data.py

#__name__ and __main__ are used to check if the script is being run directly or imported as a module.

'''
if __name__ == "__main__":
    build_sheet(PDC_Circuit_Strings, "Z_def_pagetest")
    print("wrote Z_def_pagetest.html and Z_def_pagetest.pdf")

long_circuit = {
    "circuit_number": 99,
    "circuit_name": "Page break test",
    "drawing_number": "TEST",
    "type": "Test",
    "circuit_strings": [PDC_Circuit_Strings[0]["circuit_strings"][0]] * 1000
}

build_sheet([long_circuit], "Z_1000_pagetest")
print("wrote Z_1000_pagetest.html and Z_1000_pagetest.pdf")
'''

