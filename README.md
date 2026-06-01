# Skid Checkout Sheet Builder

Streamlit app for building printed commissioning/checkout sheets for industrial skids.
Replaces a legacy VBA Excel macro tool.

## Run

```bash
~/.local/bin/streamlit run app.py
```

Opens at http://localhost:8501

## Stack
- Python / Streamlit — UI
- Jinja2 + WeasyPrint — PDF generation (in progress)

## Status
The form is complete. PDF output is not yet wired up — the Build tab shows a placeholder.
