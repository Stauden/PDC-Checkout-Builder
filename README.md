# Skid Checkout Sheet Builder

Streamlit app for building printed commissioning/checkout sheets for PDCs.
Replaces a legacy VBA Excel macro tool.

## Linux Installation

1. Install Python — most distros include it, check with:
   ```bash
   python3 --version
   ```
   If not installed, run:
   ```bash
   sudo apt install python3 python3-pip   # Debian/Ubuntu
   sudo dnf install python3               # Fedora
   sudo pacman -S python python-pip       # Arch
   ```

2. Create and activate a virtual environment in the project folder:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   Your prompt now shows a `(.venv)` prefix. Do steps 2–3 once; after that
   just reactivate with `source .venv/bin/activate` in each new terminal.

3. Install Streamlit into the environment:
   ```bash
   pip install -U streamlit
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

Your browser will open automatically at http://localhost:8501
When you're done, run `deactivate` to leave the environment.

## Windows Installation

1. Install Python — go to https://www.python.org/downloads/ and download the latest version. Run the installer and on the first screen check **"Add python.exe to PATH"**, then click Install Now.

2. Open PowerShell in the project folder — in File Explorer, navigate to the project folder, click the address bar, type `powershell`, and press Enter.

3. Create and activate a virtual environment in the project folder:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   Your prompt now shows a `(.venv)` prefix. Do steps 3–4 once; after that
   just reactivate with `.\.venv\Scripts\Activate.ps1` in each new session.

   If PowerShell blocks the script with an execution-policy error, run this
   once in the same window and retry, or use `.\.venv\Scripts\activate.bat`
   from cmd.exe instead:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   ```

4. Install Streamlit into the environment:
   ```powershell
   pip install -U streamlit
   ```

5. Run the app:
   ```powershell
   streamlit run app.py
   ```

Your browser will open automatically at http://localhost:8501
When you're done, run `deactivate` to leave the environment.

## Stack
- Python / Streamlit — UI
- Jinja2 + WeasyPrint — PDF generation (in progress)

## Status
The form is complete. PDF output is not yet wired up — the Build tab shows a placeholder.
