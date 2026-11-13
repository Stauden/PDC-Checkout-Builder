from fastapi import Request, FastAPI, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from build import BASE_DIR, render_sheet, write_pdf_byte

#for test button
import copy
from data import PDC_Circuit_Strings
'''
Start: uvicorn main:app --reload
Start: uv run fastapi dev main.py
'''

app = FastAPI() #holds the routing table
templates = Jinja2Templates(directory=BASE_DIR / "templates")

circuits = []

circuit = {
    #headers
    "circuit_name": "",
    "drawing_number": "",
    "type": "",
    #elements
    "circuit_strings": []
}

empty_element = {
    "device_description": "", "input_terminal": "", "comment": "",
    "output_terminal": "", "output_wire": "", "logic_gate": "", 
}

def empty_circuit():
    return {
        "circuit_name": "",
        "drawing_number": "",
        "type": "",
        "circuit_strings": []
    }

#Home Page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"title": "Home"})

#Circuit Form Page
@app.get("/circuit_form", response_class=HTMLResponse)
def circuit_form(request: Request):
    return templates.TemplateResponse(request, "circuit_form.html", {
        "circuit_i": circuit,
        "title": "Circuit Form",
        "edit_element": empty_element,
        "edit_index": "",
        "circuits": circuits
        
        })

#View Circuit Page
@app.get("/circuit_form/view_circuit", response_class=HTMLResponse)
def view_circuit():
    view = render_sheet([circuit])
    links = """
      <a href="/circuit_form">Back to Form</a> |
      <a href="/circuit_form/download_circuit">Download PDF</a>
    """
    return links + view

#View Circuits Page
@app.get("/circuit_form/view_circuits", response_class=HTMLResponse)
def view_circuits():
    view = render_sheet(circuits)
    links = """
      <a href="/circuit_form">Back to Form</a> |
      <a href="/circuit_form/download_circuits">Download PDF</a>
    """
    return links + view


#Download Circuit Page
@app.get("/circuit_form/download_circuit")
def download_circuit():
    html = render_sheet([circuit])
    pdf_bytes = write_pdf_byte(html)
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="web_output_circuit.pdf"'}
    )

#Download Circuits Page
@app.get("/circuit_form/download_circuits")
def download_circuits():
    html = render_sheet(circuits)
    pdf_bytes = write_pdf_byte(html)
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="web_output_circuits.pdf"'}
    )

#Deleteing rows
@app.get("/circuit_form/delete/{index}")
def delete_circuit_row(index: int):
    if 0 <= index < len(circuit["circuit_strings"]):
        del circuit["circuit_strings"][index]
    return RedirectResponse("/circuit_form", status_code=303)

#Editing rows
@app.get("/circuit_form/edit/{index}", response_class=HTMLResponse)
def edit_circuit_row(request: Request, index: int):
    if not(0 <= index < len(circuit["circuit_strings"])):
        return RedirectResponse("/circuit_form", status_code=303)
    
    element = circuit["circuit_strings"][index]
    return templates.TemplateResponse(request, "circuit_form.html", {
        "circuit_i": circuit, 
        "edit_index": index, 
        "edit_element": element, 
        "title": "Circuit Form",
        "circuits": circuits
        })

#Circuit Headers Submit
@app.post("/circuit_form/circuit_headers_submit")
def circuit_headers_submit( circuit_name: str = Form(...), drawing_number: str = Form(...), type: str = Form(...)):
    circuit["circuit_name"] = circuit_name
    circuit["drawing_number"] = drawing_number
    circuit["type"] = type
    return RedirectResponse("/circuit_form", status_code=303)

#populate with test data
@app.post("/circuit_form/populate")
def populate_circuit():
    circuit.update(copy.deepcopy(PDC_Circuit_Strings[0]))
    return RedirectResponse("/circuit_form", status_code=303)

#Circuit Elements Submit
@app.post("/circuit_form/circuit_element_submit")
def circuit_element_submit(device_description: str = Form(...), input_terminal: str = Form(...), comment: str = Form(...), output_terminal: str = Form(...), output_wire: str = Form(...), logic_gate: str = Form(...), index: str = Form("")):
    new_element = {
        "device_description": device_description,
        "input_terminal": input_terminal,
        "comment": comment,
        "output_terminal": output_terminal,
        "output_wire": output_wire,
        "logic_gate": logic_gate
    }
    if index == "":
        circuit["circuit_strings"].append(new_element)
    else:
        circuit["circuit_strings"][int(index)] = new_element
    return RedirectResponse("/circuit_form", status_code=303) #303 means make a get request to that URL. 

#Submit Circuit to List
@app.post("/circuit_form/submit_circuit")
def submit_circuit():
    circuits.append(copy.deepcopy(circuit)) #Store Circuit
    circuit.update(empty_circuit()) #Clear current circuit after saving
    return RedirectResponse("/circuit_form", status_code=303)
