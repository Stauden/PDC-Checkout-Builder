from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from build import BASE_DIR, build_sheet

'''
Start: uvicorn main:app --reload
'''

#ELEMENTS Holds a list of dictionaries, each dictionary represents a circuit element with its properties.
ELEMENTS = []
app = FastAPI()

#
@app.get("/circuit_form", response_class=HTMLResponse)
def circuit_form():
    rows = ""
    for e in ELEMENTS:
        rows += "<tr><td>" + e["device_description"] + "</td><td>" + e["input_terminal"] + "</td><td>" + e["comment"] + "</td><td>" + e["output_terminal"] + "</td><td>" + e["output_wire"] + "</td><td>" + e["logic_gate"] + "</td></tr>" 
    return f"""
    <form method="post" action="/circuit_form/circuit_submit">
      <input name="device_description" placeholder="Device Description"> <br>
      <input name="input_terminal" placeholder="Input Terminal"> <br>
      <input name="comment" placeholder="Comment"> <br>
      <input name="output_terminal" placeholder="Output Terminal"> <br>
      <input name="output_wire" placeholder="Output Wire"> <br>
      <select name="logic_gate" placeholder="Logic Gate">
        <option value="OR">OR</option>
        <option value="AND">AND</option>
        <option value="END">END</option>
      </select> <br>
      <button type="submit">Submit</button><br>
      <table>
        {rows}
      </table>
    </form>
    <a href="/circuit_form/view_circuit">View Circuit</a>
    """

#
@app.get("/circuit_form/view_circuit", response_class=HTMLResponse)
def view_circuit():
    view = build_sheet([get_circuit()], "test_user_defined_circuit")
    links = """
      <a href="/circuit_form">Back to Form</a> |
      <a href="/circuit_form/download_circuit">Download PDF</a>
    """
    return links + view

#
@app.get("/circuit_form/download_circuit")
def download_circuit():
    build_sheet([get_circuit()], "test_user_defined_circuit")
    return FileResponse(BASE_DIR.joinpath("test_user_defined_circuit.pdf"), media_type="application/pdf", filename="test_user_defined_circuit.pdf")

#
@app.post("/circuit_form/circuit_submit")
def circuit_submit(device_description: str = Form(...), input_terminal: str = Form(...), comment: str = Form(...), output_terminal: str = Form(...), output_wire: str = Form(...), logic_gate: str = Form(...)):
    new_element = {
        "device_description": device_description,
        "input_terminal": input_terminal,
        "comment": comment,
        "output_terminal": output_terminal,
        "output_wire": output_wire,
        "logic_gate": logic_gate
    }
    ELEMENTS.append(new_element)
    return RedirectResponse("/circuit_form", status_code=303) #303 means make a get request to that URL. 

#Add header elements to form
def get_circuit():
    circuit = {
      #Header elements
      "circuit_number": 1,
      "circuit_name": "User Defined Circuit",
      "drawing_number": "USER",
      "type": "User",
      #Circuit_String : [ {Row 1 Dict}, {Row 2 Dict}, ... ]
      "circuit_strings": ELEMENTS
    }
    return circuit