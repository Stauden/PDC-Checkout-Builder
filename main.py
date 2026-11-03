from fastapi import Request, FastAPI, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from build import BASE_DIR, render_sheet, write_pdf_byte

'''
Start: uvicorn main:app --reload
Start: uv run fastapi dev main.py
'''

circuit = {
    #headers
    "circuit_number": 1,
    "circuit_name": "",
    "drawing_number": "",
    "type": "",
    #elements
    "circuit_strings": []
}
app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")

#Home Page
@app.get("/", response_class=HTMLResponse)
def home():
    #FastAPI converts the dictionary to a JSON response automatically
    return HTMLResponse(f"<h1>Welcome to the PDC Checkout Builder API</h1><a href='/circuit_form'>Go to Circuit Form</a>")

#Circuit Form Page
@app.get("/circuit_form", response_class=HTMLResponse)
def circuit_form(request: Request):
    return templates.TemplateResponse(request, "circuit_form.html", {"html_circuit": circuit})

#View Circuit Page
@app.get("/circuit_form/view_circuit", response_class=HTMLResponse)
def view_circuit():
    view = render_sheet([circuit])
    links = """
      <a href="/circuit_form">Back to Form</a> |
      <a href="/circuit_form/download_circuit">Download PDF</a>
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

#Circuit Headers Submit
@app.post("/circuit_form/circuit_headers_submit")
def circuit_headers_submit( circuit_name: str = Form(...), drawing_number: str = Form(...), type: str = Form(...)):
    circuit["circuit_name"] = circuit_name
    circuit["drawing_number"] = drawing_number
    circuit["type"] = type
    return RedirectResponse("/circuit_form", status_code=303)

#Circuit Elements Submit
@app.post("/circuit_form/circuit_element_submit")
def circuit_element_submit(device_description: str = Form(...), input_terminal: str = Form(...), comment: str = Form(...), output_terminal: str = Form(...), output_wire: str = Form(...), logic_gate: str = Form(...)):
    new_element = {
        "device_description": device_description,
        "input_terminal": input_terminal,
        "comment": comment,
        "output_terminal": output_terminal,
        "output_wire": output_wire,
        "logic_gate": logic_gate
    }
    circuit["circuit_strings"].append(new_element)
    return RedirectResponse("/circuit_form", status_code=303) #303 means make a get request to that URL. 
