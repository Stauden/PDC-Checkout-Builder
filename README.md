# PDC Checkout Sheet Builder

A small FastAPI web app for building printed commissioning/checkout sheets for PDC switchgear permissive strings. You enter a circuit and its elements in the browser, and it produces a print-ready PDF that matches the layout of the legacy VBA Excel macro tool it replaces.

## What it does

- Enter a circuit header: circuit name, drawing number and type
- Add, edit and delete the elements of a permissive string
- View the finished checkout sheet in the browser
- Download the sheet as a letter-size PDF
- Load sample data with one click, for testing

**Current scope:** Switch Gear permissive strings, one circuit at a time. Data is kept in memory only, so stopping the server (or saving a file while running with `--reload`) clears it.

## Project structure

```
PDC-Checkout-Builder/
├── main.py                  # FastAPI app: routes, form handling, in-memory circuit data
├── build.py                 # Renders the checkout sheet HTML and generates PDFs
├── data.py                  # Two real sample circuits, used for testing
└── templates/
    ├── layout.html          # Shared page shell (Pico.css styling)
    ├── home.html            # Landing page
    ├── circuit_form.html    # Header form, element form and element table
    └── string_sheet.html    # The printable checkout sheet layout
```

## Requirements

- Python 3.10 or newer
- The Python packages: `fastapi`, `uvicorn`, `jinja2`, `python-multipart`, `weasyprint`
- WeasyPrint's system libraries (Pango/GTK). These are not Python packages and are installed separately; see the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html) for your platform.

## Installation

### Windows

1. **Install Python** from https://www.python.org/downloads/. On the installer's first screen, check **"Add python.exe to PATH"**, then click Install Now.

2. **Open PowerShell in the project folder.** In File Explorer, go to the project folder, click the address bar, type `powershell`, and press Enter.

3. **Create and activate a virtual environment:**
   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   Your prompt now starts with `(venv)`. Steps 3–5 are one-time setup; after that, just reactivate with `.\venv\Scripts\Activate.ps1` in each new terminal.

   If PowerShell blocks the script with an execution-policy error, run this once in the same window and try again:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   ```

4. **Install the Python packages:**
   ```powershell
   pip install fastapi uvicorn jinja2 python-multipart weasyprint
   ```

5. **Install WeasyPrint's system libraries** by following the Windows section of the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html). If this step is missing, importing WeasyPrint fails with an error about `libgobject-2.0-0`.

### Linux

1. **Check Python is installed:**
   ```bash
   python3 --version
   ```
   If it isn't, install it with your package manager (for example `sudo apt install python3 python3-venv python3-pip` on Debian/Ubuntu).

2. **Create and activate a virtual environment** in the project folder:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Python packages:**
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart weasyprint
   ```

4. **Install WeasyPrint's system libraries** (Pango) for your distribution, as listed in the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).

## Running the app

With the virtual environment active, from the project folder:

```bash
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. `--reload` restarts the server whenever you save a file, which is handy while developing but also clears the in-memory circuit. Press **Ctrl+C** to stop the server, and run `deactivate` to leave the virtual environment.

## Using it

1. Open **Circuit Form** from the home page.
2. Fill in the **Circuit Header** and click **Save Header**.
3. Add each element in order with **Add Element**. The last element is treated as the string's ending and prints as the two-row Wire # / Ending Terminal block, so its Input Terminal and Logic can be left blank.
4. Use **Edit** and **Delete** in the Elements table to fix mistakes. While editing, the row is highlighted and the button reads **Update**.
5. Click **View Sheet** to check the layout, then **Download PDF**.

**Load test data** fills the form with a real sample circuit from `data.py`.

## Testing the sheet without the web app

```bash
python build.py
```

This renders the sample circuits in `data.py` straight to `test_output.pdf`. Run it after changing `string_sheet.html` to confirm the sheet still comes out right.

## Notes

- **GLib-GIO warnings on Windows.** Messages like `Unexpectedly, UWP app ... supports N extensions but has no verbs` appear when WeasyPrint loads. They come from the GTK libraries and are harmless.
- **The sheet and the web pages are styled separately.** `string_sheet.html` has its own print CSS (page size, borders, page breaks). Keep web styling such as Pico.css out of it.

## Stack

- **FastAPI** + **Uvicorn**: web server and routes
- **Jinja2**: web page templates and the checkout sheet template
- **WeasyPrint**: HTML to PDF
- **Pico.css**: web page styling

## Roadmap

- Multiple circuits per sheet
- Save and load jobs as JSON, so work survives a restart
- Repeat the circuit title on continuation pages, and add page numbers
- Job cover page (skid, job number, customer, unit number, PLC serial)