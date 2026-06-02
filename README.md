# Skid Checkout Sheet Builder

Streamlit app for building printed commissioning/checkout sheets for industrial skids.
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

2. Install Streamlit:
   ```bash
   pip3 install streamlit
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

Your browser will open automatically at http://localhost:8501

## Windows Installation

1. Install Python — go to https://www.python.org/downloads/ and download the latest version. Run the installer and on the first screen check **"Add python.exe to PATH"**, then click Install Now.

2. Open PowerShell in the project folder — in File Explorer, navigate to the project folder, click the address bar, type `powershell`, and press Enter.

3. Install Streamlit:
   ```powershell
   pip install streamlit
   ```

4. Run the app:
   ```powershell
   streamlit run app.py
   ```
   If that command is not recognized, use:
   ```powershell
   py -m streamlit run app.py
   ```

Your browser will open automatically at http://localhost:8501

## Stack
- Python / Streamlit — UI
- Jinja2 + WeasyPrint — PDF generation (in progress)

## Status
The form is complete. PDF output is not yet wired up — the Build tab shows a placeholder.
