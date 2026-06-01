"""
Skid Checkout Sheet Builder
Run: streamlit run app.py
"""

import streamlit as st

from models import (
    JobConfig, JobInfo, Pump, AnalogInstrument, DigitalIO,
    SwitchGearItem, Bucket, ATSUnit, HVACConfig, MiscItem,
    PUMP_VFD_OPTIONS, ANALOG_TYPE_OPTIONS, ANALOG_SUBTYPE_OPTIONS,
    DIGITAL_TYPE_OPTIONS, DIGITAL_SUBTYPE_OPTIONS,
    SG_TYPE_OPTIONS, SG_ITEM_SUBTYPE_OPTIONS, SG_ITEM_SUBTYPE_IDX,
    BUCKET_VFD_OPTIONS, BUCKET_TYPE_OPTS, ATS_TYPE_OPTIONS,
)

st.set_page_config(page_title="Skid Sheet Builder", page_icon="📋", layout="wide")


# ── session state init ────────────────────────────────────────────────────────

def _init_state():
    defaults = {
        "started": False,
        "pumps": [], "analogs": [], "digitals": [],
        "switchgear": [], "buckets": [], "ats": [],
        "hvac_enabled": False, "hvac_count": 1,
        "misc": [],
        "drawing_number": "", "job_number": "", "customer_name": "",
        "unit_number": "", "plc_serial": "",
        "wet_test": False, "has_pdc": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init_state()


def _apply_config(cfg: JobConfig):
    st.session_state.drawing_number = cfg.job.drawing_number
    st.session_state.job_number     = cfg.job.job_number
    st.session_state.customer_name  = cfg.job.customer_name
    st.session_state.unit_number    = cfg.job.unit_number
    st.session_state.plc_serial     = cfg.job.plc_serial
    st.session_state.wet_test       = cfg.job.wet_test
    st.session_state.has_pdc        = cfg.job.has_pdc
    st.session_state.pumps          = cfg.pumps
    st.session_state.analogs        = cfg.analogs
    st.session_state.digitals       = cfg.digitals
    st.session_state.switchgear     = cfg.switchgear
    st.session_state.buckets        = cfg.buckets
    st.session_state.ats            = cfg.ats
    st.session_state.hvac_enabled   = cfg.hvac.enabled
    st.session_state.hvac_count     = cfg.hvac.count
    st.session_state.misc           = cfg.misc
    st.session_state.started        = True


# ── landing page ──────────────────────────────────────────────────────────────

if not st.session_state.started:
    st.title("Skid Checkout Sheet Builder")
    st.write("Generate a print-ready commissioning sheet for any skid configuration.")
    st.write("")
    if st.button("New Sheet", type="primary"):
        _apply_config(JobConfig())
    st.stop()


# ── main editor (shown after landing page choice) ─────────────────────────────

st.title("Skid Checkout Sheet Builder")

if st.button("← Back / New Job", key="back_btn"):
    st.session_state.started = False
    st.rerun()

tabs = st.tabs([
    "Job Info", "Pumps", "Analog", "Digital",
    "SwitchGear", "Buckets", "ATS / HVAC", "Misc", "Build"
])

# ── Tab: Job Info ─────────────────────────────────────────────────────────────
with tabs[0]:
    st.subheader("Job Information")
    c1, c2 = st.columns(2)
    st.session_state.drawing_number = c1.text_input("Drawing Number",    value=st.session_state.drawing_number)
    st.session_state.job_number     = c1.text_input("A&E Job Number",    value=st.session_state.job_number)
    st.session_state.customer_name  = c1.text_input("Customer Name",     value=st.session_state.customer_name)
    st.session_state.unit_number    = c2.text_input("Unit Number",       value=st.session_state.unit_number)
    st.session_state.plc_serial     = c2.text_input("A&E PLC Serial #",  value=st.session_state.plc_serial)
    st.session_state.wet_test       = c2.checkbox("Include Wet Test",    value=st.session_state.wet_test)
    st.session_state.has_pdc        = c2.checkbox("Has PDC",             value=st.session_state.has_pdc)


# ── Tab: Pumps ────────────────────────────────────────────────────────────────
with tabs[1]:
    st.subheader("Pumps / Motors")
    if st.button("+ Add Pump"):
        st.session_state.pumps.append(Pump())

    del_p = None
    for i, p in enumerate(st.session_state.pumps):
        with st.expander(f"Pump #{i+1} — {p.name or '(unnamed)'}", expanded=True):
            r1 = st.columns([2, 2, 2, 1])
            p.name     = r1[0].text_input("Device Tag",       value=p.name,     key=f"p_name_{i}")
            p.location = r1[1].text_input("Location / Panel", value=p.location, key=f"p_loc_{i}")
            p.vfd_type = r1[2].selectbox("Control / VFD Type", PUMP_VFD_OPTIONS,
                             index=PUMP_VFD_OPTIONS.index(p.vfd_type) if p.vfd_type in PUMP_VFD_OPTIONS else 0,
                             key=f"p_vfd_{i}")
            if r1[3].button("Delete", key=f"p_del_{i}"):
                del_p = i
            r2 = st.columns(3)
            p.pump_type      = r2[0].text_input("Sub-Type (e.g. Charge)", value=p.pump_type,      key=f"p_type_{i}")
            p.command_source = r2[1].text_input("Command Source",          value=p.command_source, key=f"p_cmd_{i}")
            p.feedback       = r2[2].text_input("Feedback / Status",       value=p.feedback,       key=f"p_fbs_{i}")
    if del_p is not None:
        st.session_state.pumps.pop(del_p); st.rerun()
    if not st.session_state.pumps:
        st.info("No pumps added yet.")


# ── Tab: Analog ───────────────────────────────────────────────────────────────
with tabs[2]:
    st.subheader("Analog Instruments")
    if st.button("+ Add Analog"):
        st.session_state.analogs.append(AnalogInstrument())

    del_a = None
    for i, a in enumerate(st.session_state.analogs):
        with st.expander(f"Analog #{i+1} — {a.name or '(unnamed)'}", expanded=True):
            r1 = st.columns([2, 2, 2, 1])
            a.name     = r1[0].text_input("Device Tag",       value=a.name,     key=f"a_name_{i}")
            a.location = r1[1].text_input("Location / Panel", value=a.location, key=f"a_loc_{i}")
            a.type     = r1[2].selectbox("Type", ANALOG_TYPE_OPTIONS,
                             index=ANALOG_TYPE_OPTIONS.index(a.type) if a.type in ANALOG_TYPE_OPTIONS else 0,
                             key=f"a_type_{i}")
            if r1[3].button("Delete", key=f"a_del_{i}"):
                del_a = i
            r2 = st.columns([2, 1, 1, 1])
            a.subtype = r2[0].selectbox("Signal Type", ANALOG_SUBTYPE_OPTIONS,
                            index=ANALOG_SUBTYPE_OPTIONS.index(a.subtype) if a.subtype in ANALOG_SUBTYPE_OPTIONS else 0,
                            key=f"a_sub_{i}")
            a.unit = r2[1].text_input("Units",     value=a.unit, key=f"a_unit_{i}")
            a.lrv  = r2[2].text_input("LRV (0%)",  value=a.lrv,  key=f"a_lrv_{i}")
            a.urv  = r2[3].text_input("URV (100%)", value=a.urv,  key=f"a_urv_{i}")
    if del_a is not None:
        st.session_state.analogs.pop(del_a); st.rerun()
    if not st.session_state.analogs:
        st.info("No analog instruments added yet.")


# ── Tab: Digital ──────────────────────────────────────────────────────────────
with tabs[3]:
    st.subheader("Digital I/O")
    if st.button("+ Add Digital"):
        st.session_state.digitals.append(DigitalIO())

    del_d = None
    for i, d in enumerate(st.session_state.digitals):
        with st.expander(f"Digital #{i+1} — {d.name or '(unnamed)'}", expanded=True):
            r1 = st.columns([2, 2, 2, 1])
            d.name     = r1[0].text_input("Device Tag",       value=d.name,     key=f"d_name_{i}")
            d.location = r1[1].text_input("Location / Panel", value=d.location, key=f"d_loc_{i}")
            d.type     = r1[2].selectbox("Type", DIGITAL_TYPE_OPTIONS,
                             index=DIGITAL_TYPE_OPTIONS.index(d.type) if d.type in DIGITAL_TYPE_OPTIONS else 0,
                             key=f"d_type_{i}")
            if r1[3].button("Delete", key=f"d_del_{i}"):
                del_d = i
            r2 = st.columns([2, 2, 2])
            d.subtype        = r2[0].selectbox("Contact Type", DIGITAL_SUBTYPE_OPTIONS,
                                  index=DIGITAL_SUBTYPE_OPTIONS.index(d.subtype) if d.subtype in DIGITAL_SUBTYPE_OPTIONS else 0,
                                  key=f"d_sub_{i}")
            d.command_source = r2[1].text_input("Command Source",      value=d.command_source, key=f"d_cmd_{i}")
            d.feedback       = r2[2].text_input("Feedback / Status",   value=d.feedback,       key=f"d_fbs_{i}")
            r3 = st.columns(3)
            d.rising_sp  = r3[0].text_input("Rising SP",  value=d.rising_sp,  key=f"d_rsp_{i}")
            d.falling_sp = r3[1].text_input("Falling SP", value=d.falling_sp, key=f"d_fsp_{i}")
            d.units      = r3[2].text_input("Units",       value=d.units,      key=f"d_units_{i}")
    if del_d is not None:
        st.session_state.digitals.pop(del_d); st.rerun()
    if not st.session_state.digitals:
        st.info("No digital I/O added yet.")


# ── Tab: SwitchGear ───────────────────────────────────────────────────────────
with tabs[4]:
    st.subheader("Switch Gear / Permissive Strings")
    st.caption("Build up circuits top-to-bottom: start each circuit with a **Permissive String** header, "
               "add **PS Items** for each device, then close with a **PS Ending**.")

    if st.button("+ Add Row"):
        st.session_state.switchgear.append(SwitchGearItem())

    del_sg = None
    for i, sg in enumerate(st.session_state.switchgear):
        label = f"#{i+1} [{SG_TYPE_OPTIONS[min(sg.sg_type, 2)]}] {sg.name or sg.device_desc or '(unnamed)'}"
        with st.expander(label, expanded=True):
            r1 = st.columns([2, 2, 1])
            raw_type = r1[0].selectbox("Row Type", SG_TYPE_OPTIONS,
                           index=min(max(sg.sg_type - (1 if sg.sg_type <= 1 else 0), 0), 2),
                           key=f"sg_type_{i}")
            # Map display index back to raw type index
            sg.sg_type = [1, 2, 3][SG_TYPE_OPTIONS.index(raw_type)]
            if r1[2].button("Delete", key=f"sg_del_{i}"):
                del_sg = i

            if sg.sg_type <= 1:  # Permissive String header
                r2 = st.columns([2, 2])
                sg.name           = r2[0].text_input("Circuit Name",    value=sg.name,           key=f"sg_name_{i}")
                sg.drawing_number = r2[1].text_input("Drawing Number",  value=sg.drawing_number, key=f"sg_dwg_{i}")
                r3 = st.columns([2, 2])
                sg.logic_desc     = r3[0].text_input("Type / Logic",    value=sg.logic_desc,     key=f"sg_logic_{i}")
                sg.prefill_comment= r3[1].text_input("Comment",         value=sg.prefill_comment,key=f"sg_cmt_{i}")
                r4 = st.columns([2, 2])
                sg.wire_tb        = r4[0].text_input("Input Terminal",  value=sg.wire_tb,        key=f"sg_wtb_{i}")
                sg.device_tb      = r4[1].text_input("Output Terminal", value=sg.device_tb,      key=f"sg_dtb_{i}")

            elif sg.sg_type == 2:  # PS Item
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


# ── Tab: Buckets ──────────────────────────────────────────────────────────────
with tabs[5]:
    st.subheader("Power Supply Buckets")
    if st.button("+ Add Bucket"):
        st.session_state.buckets.append(Bucket())

    del_b = None
    for i, b in enumerate(st.session_state.buckets):
        with st.expander(f"Bucket #{i+1} — {b.name or '(unnamed)'}", expanded=True):
            r1 = st.columns([2, 2, 2, 1])
            b.name     = r1[0].text_input("Bucket Tag",       value=b.name,     key=f"bk_name_{i}")
            b.location = r1[1].text_input("IP Address / LOC", value=b.location, key=f"bk_loc_{i}")
            b.vfd_type = r1[2].selectbox("Control Type", BUCKET_VFD_OPTIONS,
                             index=BUCKET_VFD_OPTIONS.index(b.vfd_type) if b.vfd_type in BUCKET_VFD_OPTIONS else 0,
                             key=f"bk_vfd_{i}")
            if r1[3].button("Delete", key=f"bk_del_{i}"):
                del_b = i

            type_opts = BUCKET_TYPE_OPTS.get(b.vfd_type, ["Standard"])
            b.bucket_type = min(b.bucket_type, len(type_opts) - 1)
            b.bucket_type = type_opts.index(
                st.selectbox("Sub-Type", type_opts, index=b.bucket_type, key=f"bk_sub_{i}")
            )
            r2 = st.columns(2)
            b.command_source = r2[0].text_input("Command Source",    value=b.command_source, key=f"bk_cmd_{i}")
            b.feedback       = r2[1].text_input("Feedback / Status", value=b.feedback,       key=f"bk_fbs_{i}")
    if del_b is not None:
        st.session_state.buckets.pop(del_b); st.rerun()
    if not st.session_state.buckets:
        st.info("No buckets added yet.")


# ── Tab: ATS / HVAC ───────────────────────────────────────────────────────────
with tabs[6]:
    st.subheader("ATS — Automatic Transfer Switch")
    if st.button("+ Add ATS"):
        st.session_state.ats.append(ATSUnit())

    del_ats = None
    for i, a in enumerate(st.session_state.ats):
        with st.expander(f"ATS #{i+1} — {a.ats_type}", expanded=True):
            c1, c2, c3 = st.columns([2, 2, 1])
            a.ats_type = c1.selectbox("ATS Type", ATS_TYPE_OPTIONS,
                            index=ATS_TYPE_OPTIONS.index(a.ats_type) if a.ats_type in ATS_TYPE_OPTIONS else 0,
                            key=f"ats_type_{i}")
            a.name     = c2.text_input("Tag / Name", value=a.name, key=f"ats_name_{i}")
            if c3.button("Delete", key=f"ats_del_{i}"):
                del_ats = i
    if del_ats is not None:
        st.session_state.ats.pop(del_ats); st.rerun()

    st.divider()
    st.subheader("HVAC — MarVair Units")
    st.session_state.hvac_enabled = st.checkbox("Include HVAC section", value=st.session_state.hvac_enabled)
    if st.session_state.hvac_enabled:
        st.session_state.hvac_count = st.number_input(
            "Number of MarVair units", min_value=1, max_value=20,
            value=st.session_state.hvac_count, step=1)


# ── Tab: Misc ─────────────────────────────────────────────────────────────────
with tabs[7]:
    st.subheader("Miscellaneous Items")
    if st.button("+ Add Misc Item"):
        st.session_state.misc.append(MiscItem())

    del_m = None
    for i, m in enumerate(st.session_state.misc):
        with st.expander(f"Misc #{i+1} — {m.name or '(unnamed)'}", expanded=True):
            c1, c2, c3, c4 = st.columns([2, 2, 2, 1])
            m.name     = c1.text_input("Name / Tag",  value=m.name,     key=f"m_name_{i}")
            m.location = c2.text_input("Location",    value=m.location, key=f"m_loc_{i}")
            m.protocol = c3.text_input("Protocol",    value=m.protocol, key=f"m_pro_{i}")
            if c4.button("Delete", key=f"m_del_{i}"):
                del_m = i
    if del_m is not None:
        st.session_state.misc.pop(del_m); st.rerun()


# ── Tab: Build ────────────────────────────────────────────────────────────────
with tabs[8]:
    st.subheader("Build & Download")
    st.write(f"**Pumps:** {len(st.session_state.pumps)}  "
             f"**Analogs:** {len(st.session_state.analogs)}  "
             f"**Digitals:** {len(st.session_state.digitals)}  "
             f"**SwitchGear rows:** {len(st.session_state.switchgear)}  "
             f"**Buckets:** {len(st.session_state.buckets)}  "
             f"**ATS:** {len(st.session_state.ats)}  "
             f"**HVAC:** {'Yes ×' + str(st.session_state.hvac_count) if st.session_state.hvac_enabled else 'No'}  "
             f"**Misc:** {len(st.session_state.misc)}")
    st.divider()
    st.info("PDF generation coming soon (Jinja2 + WeasyPrint).")
