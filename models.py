from dataclasses import dataclass, field

# ── SwitchGear ─────────────────────────────────────────────────────────────────
SG_TYPE_OPTIONS = ["Permissive String", "PS Item", "PS Ending"]
SG_ITEM_SUBTYPE_OPTIONS = ["General Purpose", "First OR", "Middle OR", "Last OR"]
SG_ITEM_SUBTYPE_IDX = {"General Purpose": 0, "First OR": 2, "Middle OR": 3, "Last OR": 4}


# ── Dataclasses ────────────────────────────────────────────────────────────────
@dataclass
class JobInfo:
    drawing_number: str = ""
    job_number: str = ""
    customer_name: str = ""
    unit_number: str = ""
    plc_serial: str = ""

@dataclass
class SwitchGearItem:
    sg_type: int = 0          # index into SG_TYPE_OPTIONS
    subtype: int = 0
    name: str = ""
    drawing_number: str = ""
    logic_desc: str = ""
    device_desc: str = ""
    device_tb: str = ""
    prefill_comment: str = ""
    wire_tb: str = ""

@dataclass
class JobConfig:
    job: JobInfo = field(default_factory=JobInfo)
    switchgear: list = field(default_factory=list)
    