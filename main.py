from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# test run: uvicorn main:app --reload
@app.get("/test", response_class=HTMLResponse)
def test_form():
    return """
    <form method="post" action="/test">
      <input name="device">
      <input name="terminal">
      <button type="submit">Go</button>
    </form>
    """


@app.post("/test")
def test_submit(device: str = Form(...), terminal: str = Form(...)):
    return {"device": device, "terminal": terminal}