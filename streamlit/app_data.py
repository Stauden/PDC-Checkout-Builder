"""
PDC Checkout Sheet Builder - data.py edition

Edits the circuit structure defined in ../data.py (PDC_Circuit_Strings) and
renders it through ../templates/string_sheet.html.

Run from the project root:
    streamlit run streamlit/app_data.py
"""

import copy
import sys
from pathlib import Path

import streamlit as st
from jinja2 import Environment, FileSystemLoader, StrictUndefined

# data.py / templates/ live one level up from this file
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from data import PDC_Circuit_Strings  # noqa: E402

# build.py is intentionally not imported: it runs a page-break test build at
# import time, so the Jinja environment is recreated here instead.
env = Environment(
    loader=FileSystemLoader(BASE_DIR.joinpath("templates")),
    undefined=StrictUndefined,
)

# Header keys of a circuit dict, and the row keys of each circuit_strings entry
CIRCUIT_HEADERS = ["circuit_number", "circuit_name", "drawing_number", "type"]
ROW_FIELDS = [
    "device_description",
    "input_terminal",
    "comment",
    "output_terminal",
    "output_wire",
    "logic_gate",
]
LOGIC_GATES = ["", "AND", "OR", "NOT"]

st.set_page_config(page_title="PDC Checkout Sheet Builder", page_icon=":gear:", layout="wide")


# -- helpers -------------------------------------------------------------------
def _blank_row():
    return {field: "" for field in ROW_FIELDS}


def _blank_circuit(number):
    return {
        "circuit_number": number,
        "circuit_name": "",
        "drawing_number": "",
        "type": "",
        "circuit_strings": [_blank_row()],
    }


def _normalize(circuits):
    """Copy incoming circuits and make sure every expected key exists."""
    cleaned = []
    for circuit in copy.deepcopy(circuits):
        for key in CIRCUIT_HEADERS:
            circuit.setdefault(key, "")
        circuit["circuit_strings"] = [
            {field: str(row.get(field, "")) for field in ROW_FIELDS}
            for row in circuit.get("circuit_strings", [])
        ]
        cleaned.append(circuit)
    return cleaned


def _rows_from_editor(result):
    """st.data_editor hands back a list or a DataFrame depending on the input."""
    rows = result.to_dict("records") if hasattr(result, "to_dict") else list(result)
    return [{field: str(row.get(field, "") or "") for field in ROW_FIELDS} for row in rows]


def _init_state():
    if "circuits" not in st.session_state:
        st.session_state.circuits = _normalize(PDC_Circuit_Strings)
    if "selected" not in st.session_state:
        st.session_state.selected = 0


_init_state()
circuits = st.session_state.circuits

# -- sidebar -------------------------------------------------------------------
with st.sidebar:
    st.header("Circuits")

    if circuits:
        labels = [
            f"#{c['circuit_number']} - {c['circuit_name'] or '(unnamed)'}" for c in circuits
        ]
        st.session_state.selected = st.radio(
            "Select a circuit",
            options=range(len(circuits)),
            format_func=lambda i: labels[i],
            index=min(st.session_state.selected, len(circuits) - 1),
        )
    else:
        st.info("No circuits yet.")

    st.divider()
    if st.button("+ Add Circuit", width="stretch"):
        next_number = max((c["circuit_number"] for c in circuits), default=0)
        circuits.append(_blank_circuit(next_number + 1 if isinstance(next_number, int) else 1))
        st.session_state.selected = len(circuits) - 1
        st.rerun()

    if st.button("Reload from data.py", width="stretch"):
        st.session_state.circuits = _normalize(PDC_Circuit_Strings)
        st.session_state.selected = 0
        st.rerun()

    if st.button("Clear All", width="stretch"):
        st.session_state.circuits = []
        st.session_state.selected = 0
        st.rerun()

# -- main ----------------------------------------------------------------------
st.title("PDC Checkout Sheet Builder")
st.caption("Circuit data loaded from `data.py` - edit below, then build the sheet.")

edit_tab, build_tab = st.tabs(["Edit Circuit", "Build"])

with edit_tab:
    if not circuits:
        st.info("Add a circuit from the sidebar to get started.")
    else:
        idx = st.session_state.selected
        circuit = circuits[idx]

        st.subheader(f"Circuit #{circuit['circuit_number']}")

        c1, c2 = st.columns(2)
        circuit["circuit_number"] = c1.number_input(
            "Circuit Number",
            value=int(circuit["circuit_number"]) if str(circuit["circuit_number"]).isdigit() else 1,
            min_value=1,
            step=1,
            key=f"num_{idx}",
        )
        circuit["circuit_name"] = c2.text_input(
            "Circuit Name", value=circuit["circuit_name"], key=f"name_{idx}"
        )
        circuit["drawing_number"] = c1.text_input(
            "Drawing Number", value=circuit["drawing_number"], key=f"dwg_{idx}"
        )
        circuit["type"] = c2.text_input("Type", value=circuit["type"], key=f"type_{idx}")

        st.divider()
        st.subheader("Circuit String Rows")
        st.caption(
            "One row per device, in order. The **last row** renders as the ending block "
            "(device description, comment, ending terminal and wire number only)."
        )

        edited = st.data_editor(
            circuit["circuit_strings"] or [_blank_row()],
            num_rows="dynamic",
            width="stretch",
            key=f"rows_{idx}",
            column_config={
                "device_description": st.column_config.TextColumn("Device Description", width="large"),
                "input_terminal": st.column_config.TextColumn("Input Terminal"),
                "comment": st.column_config.TextColumn("Comment", width="large"),
                "output_terminal": st.column_config.TextColumn("Output Terminal"),
                "output_wire": st.column_config.TextColumn("Output Wire #"),
                "logic_gate": st.column_config.SelectboxColumn("Logic", options=LOGIC_GATES),
            },
        )
        circuit["circuit_strings"] = _rows_from_editor(edited)

        if st.button("Delete This Circuit", key=f"del_{idx}"):
            circuits.pop(idx)
            st.session_state.selected = max(0, idx - 1)
            st.rerun()

with build_tab:
    st.subheader("Build & Download")
    total_rows = sum(len(c["circuit_strings"]) for c in circuits)
    st.write(f"**Circuits:** {len(circuits)}  |  **String rows:** {total_rows}")

    if not circuits:
        st.warning("Nothing to build yet.")
        st.stop()

    html = env.get_template("string_sheet.html").render(circuits=circuits)

    st.download_button(
        "Download HTML",
        data=html,
        file_name="string_sheet.html",
        mime="text/html",
    )

    if st.button("Generate PDF"):
        try:
            from weasyprint import HTML

            pdf = HTML(string=html, base_url=str(BASE_DIR)).write_pdf()
            st.download_button(
                "Download PDF", data=pdf, file_name="string_sheet.pdf", mime="application/pdf"
            )
        except Exception as exc:  # weasyprint needs GTK libs on Windows
            st.error(f"PDF generation failed: {exc}")

    st.divider()
    st.subheader("Preview")
    # Deprecated in favour of st.html, but st.html injects into the page and the
    # template's global table/td rules would restyle the app itself. The iframe
    # here keeps the sheet's CSS sandboxed.
    st.components.v1.html(html, height=800, scrolling=True)
