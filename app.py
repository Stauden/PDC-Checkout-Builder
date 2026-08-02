"""
PLC Checkout Sheet Builder
Run: streamlit run app.py
"""

import streamlit as st
from models import (
    JobConfig, JobInfo, SwitchGearItem,
    SG_TYPE_OPTIONS, SG_ITEM_SUBTYPE_OPTIONS, SG_ITEM_SUBTYPE_IDX
)

st.set_page_config(page_title="PLC Checkout Sheet Builder", page_icon=":gear:", layout="centered")

# ── session state init ────────────────────────────────────────────────────────
def _init_state():
    defaults = {
        "started": False,
        "switchgear": [],
        "drawing_number": "",
        "job_number": "",
        "customer_name": "",
        "unit_number": "",
        "plc_serial": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
            
_init_state()

def _apply_config(cfg: JobConfig):
    st.session_state["switchgear"]     = cfg.switchgear
    st.session_state["drawing_number"] = cfg.job.drawing_number
    st.session_state["job_number"]     = cfg.job.job_number
    st.session_state["customer_name"]  = cfg.job.customer_name
    st.session_state["unit_number"]    = cfg.job.unit_number
    st.session_state["plc_serial"]     = cfg.job.plc_serial
    st.session_state.started = True
    
# ── landing page ──────────────────────────────────────────────────────────────

if not st.session_state.started:
    st.title("Skid Checkout Sheet Builder")
    st.write("Generate a print-ready commissioning sheet for any skid configuration.")
    st.write("")
    
    col_new, col_load = st.columns([1, 1])
    with col_new:
        if st.button("New Sheet",):
            _apply_config(JobConfig())
            st.rerun()
    with col_load:
        if st.button("Load Sheet"):
            st.info("Load functionality coming soon (JSON + file uploader).")
        st.stop()
    
# ── main editor (shown after landing page choice) ─────────────────────────────

st.title("PLC Checkout Sheet Builder")

col_back, col_load = st.columns([1, 1])
with col_back:
    if st.button("← Back", key="back_btn"):
        st.session_state.started = False
        st.rerun()
with col_load:
    if st.button("Load Sheet Config", key="load_btn"):
        st.info("Load functionality coming soon (JSON + file uploader).")

tabs = st.tabs(["Job Info", "SwitchGear", "Build"])

# ── Tab: Job Info ─────────────────────────────────────────────────────────────
with tabs[0]:
    st.subheader("Job Information")
    c1, c2 = st.columns(2)
    st.session_state.drawing_number = c1.text_input("Drawing Number",    value=st.session_state.drawing_number)
    st.session_state.job_number     = c1.text_input("Job Number",    value=st.session_state.job_number)
    st.session_state.customer_name  = c1.text_input("Customer Name",     value=st.session_state.customer_name)
    st.session_state.unit_number    = c2.text_input("Unit Number",       value=st.session_state.unit_number)
    st.session_state.plc_serial     = c2.text_input("PLC Serial Number",  value=st.session_state.plc_serial)
# ── Tab: SwitchGear ───────────────────────────────────────────────────────────
with tabs[1]:
    st.subheader("Switch Gear / Permissive Strings")
    st.caption("Build up circuits top-to-bottom: start each circuit with a **Permissive String** header, "
               "add **PS Items** for each device, then close with a **PS Ending**.")

    if st.button("+ Add Row"):
        st.session_state.switchgear.append(SwitchGearItem())

    del_sg = None
    for i, sg in enumerate(st.session_state.switchgear):
        label = f"#{i+1} [{SG_TYPE_OPTIONS[sg.sg_type]}] {sg.name or sg.device_desc or '(unnamed)'}"
        with st.expander(label, expanded=True):
            r1 = st.columns([2, 2, 1])
            raw_type = r1[0].selectbox("Row Type", SG_TYPE_OPTIONS,
                           index=sg.sg_type,
                           key=f"sg_type_{i}")
            sg.sg_type = SG_TYPE_OPTIONS.index(raw_type)
            if r1[2].button("Delete", key=f"sg_del_{i}"):
                del_sg = i

            if sg.sg_type == 0:  # Permissive String header
                r2 = st.columns([2, 2])
                sg.name           = r2[0].text_input("Circuit Name",    value=sg.name,           key=f"sg_name_{i}")
                sg.drawing_number = r2[1].text_input("Drawing Number",  value=sg.drawing_number, key=f"sg_dwg_{i}")
                r3 = st.columns([2, 2])
                sg.logic_desc     = r3[0].text_input("Type / Logic",    value=sg.logic_desc,     key=f"sg_logic_{i}")
                sg.prefill_comment= r3[1].text_input("Comment",         value=sg.prefill_comment,key=f"sg_cmt_{i}")
                r4 = st.columns([2, 2])
                sg.wire_tb        = r4[0].text_input("Input Terminal",  value=sg.wire_tb,        key=f"sg_wtb_{i}")
                sg.device_tb      = r4[1].text_input("Output Terminal", value=sg.device_tb,      key=f"sg_dtb_{i}")

            elif sg.sg_type == 1:  # PS Item
                sub_label = next((k for k, v in SG_ITEM_SUBTYPE_IDX.items() if v == sg.subtype),
                                 SG_ITEM_SUBTYPE_OPTIONS[0])
                sub_label = r1[1].selectbox("Sub-Type", SG_ITEM_SUBTYPE_OPTIONS,
                                index=SG_ITEM_SUBTYPE_OPTIONS.index(sub_label),
                                key=f"sg_sub_{i}")
                sg.subtype = SG_ITEM_SUBTYPE_IDX[sub_label]

                r2 = st.columns([3, 3])
                sg.device_desc    = r2[0].text_input("Device Description", value=sg.device_desc,     key=f"sg_desc_{i}")
                sg.logic_desc     = r2[1].text_input("Logic",              value=sg.logic_desc,      key=f"sg_log2_{i}")
                r3 = st.columns([2, 2, 2])
                sg.wire_tb        = r3[0].text_input("Input Terminal",     value=sg.wire_tb,         key=f"sg_wtb2_{i}")
                sg.device_tb      = r3[1].text_input("Output Terminal",    value=sg.device_tb,       key=f"sg_dtb2_{i}")
                sg.prefill_comment= r3[2].text_input("Comment",            value=sg.prefill_comment, key=f"sg_cmt2_{i}")

            else:  # PS Ending
                r2 = st.columns([3, 3])
                sg.device_desc    = r2[0].text_input("Device Description", value=sg.device_desc,     key=f"sg_desc3_{i}")
                sg.device_tb      = r2[1].text_input("Ending Terminal",    value=sg.device_tb,       key=f"sg_end_{i}")
                sg.prefill_comment= r2[0].text_input("Comment",            value=sg.prefill_comment, key=f"sg_cmt3_{i}")
                sg.wire_tb        = r2[1].text_input("Wire Number",        value=sg.wire_tb,         key=f"sg_wn_{i}")

    if del_sg is not None:
        st.session_state.switchgear.pop(del_sg); st.rerun()
    if not st.session_state.switchgear:
        st.info("No switch gear rows added yet.")
        
# ── Tab: Build ────────────────────────────────────────────────────────────────
with tabs[2]:
    st.subheader("Build & Download")
    st.write(f"**SwitchGear rows:** {len(st.session_state.switchgear)}")
    st.divider()
    st.info("PDF generation coming soon (Jinja2 + WeasyPrint).")
    
