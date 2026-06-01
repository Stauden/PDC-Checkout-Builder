from dataclasses import dataclass, field

# ── Pump / Motor ───────────────────────────────────────────────────────────────
PUMP_VFD_OPTIONS = [
    "Across-The-Line",
    "Cutler-Hammer VFD",
    "Allen Bradley VFD",
    "Other VFD",
    "Contactor",
    "Mixer Motor",
    "Yaskawa VFD",
]

# ── Analog ─────────────────────────────────────────────────────────────────────
ANALOG_TYPE_OPTIONS = ["Pressure", "Temperature", "Flow", "Level", "Other"]
ANALOG_SUBTYPE_OPTIONS = ["4-20mA", "0-10V", "RTD", "Thermocouple", "Pulse", "Other"]

# ── Digital ────────────────────────────────────────────────────────────────────
DIGITAL_TYPE_OPTIONS = [
    "Pressure Switch", "Flow Switch", "Level Switch", "Temperature Switch",
    "Permissive/Status", "Vibration Switch", "Limit Switch", "Relay", "Other",
]
DIGITAL_SUBTYPE_OPTIONS = ["NO", "NC", "Analog Feedback", "Digital Feedback", "Other"]

# ── SwitchGear ─────────────────────────────────────────────────────────────────
SG_TYPE_OPTIONS = ["Permissive String", "PS Item", "PS Ending"]
SG_ITEM_SUBTYPE_OPTIONS = ["General Purpose", "First OR", "Middle OR", "Last OR"]
SG_ITEM_SUBTYPE_IDX = {"General Purpose": 0, "First OR": 2, "Middle OR": 3, "Last OR": 4}

# ── Buckets ────────────────────────────────────────────────────────────────────
BUCKET_VFD_OPTIONS = [
    "Across-The-Line",
    "VFD",
    "Soft Start",
    "E300",
    "Stratix Switch",
]
BUCKET_TYPE_OPTS = {
    "Across-The-Line": ["Standard", "w/ motor info"],
    "VFD":             ["w/o motor info", "w/ motor info", "Full VFD checkout"],
    "Soft Start":      ["w/o motor info", "w/ motor info", "Full checkout"],
    "E300":            ["Standard", "Full checkout"],
    "Stratix Switch":  ["Standard"],
}

# ── ATS ────────────────────────────────────────────────────────────────────────
ATS_TYPE_OPTIONS = ["C66", "ASCO"]

# ── Dataclasses ────────────────────────────────────────────────────────────────

@dataclass
class JobInfo:
    drawing_number: str = ""
    job_number: str = ""
    customer_name: str = ""
    unit_number: str = ""
    plc_serial: str = ""
    has_pdc: bool = False
    wet_test: bool = False


@dataclass
class Pump:
    name: str = ""
    vfd_type: str = "Across-The-Line"
    pump_type: str = ""
    location: str = ""
    command_source: str = ""
    feedback: str = ""
    wet_test_purpose: str = ""


@dataclass
class AnalogInstrument:
    name: str = ""
    type: str = "Pressure"
    subtype: str = "4-20mA"
    location: str = ""
    unit: str = ""
    lrv: str = "0"
    urv: str = "100"
    wet_test_nameplate: str = ""


@dataclass
class DigitalIO:
    name: str = ""
    type: str = "Pressure Switch"
    subtype: str = "NO"
    location: str = ""
    rising_sp: str = ""
    falling_sp: str = ""
    command_source: str = ""
    feedback: str = ""
    units: str = ""
    wet_test_nameplate: str = ""
    terminal_connections: str = ""


@dataclass
class SwitchGearItem:
    sg_type: int = 1      # 1 = Permissive String header, 2 = PS Item, 3 = PS Ending
    subtype: int = 0      # PS Item sub-type: 0=General, 2=First OR, 3=Middle OR, 4=Last OR
    name: str = ""
    drawing_number: str = ""
    logic_desc: str = ""
    device_desc: str = ""
    device_tb: str = ""
    prefill_comment: str = ""
    wire_tb: str = ""


@dataclass
class Bucket:
    name: str = ""
    vfd_type: str = "Across-The-Line"
    bucket_type: int = 0
    location: str = ""
    command_source: str = ""
    feedback: str = ""


@dataclass
class ATSUnit:
    ats_type: str = "C66"
    name: str = ""
    location: str = ""


@dataclass
class HVACConfig:
    enabled: bool = False
    count: int = 1


@dataclass
class MiscItem:
    name: str = ""
    location: str = ""
    protocol: str = ""


@dataclass
class JobConfig:
    job: JobInfo = field(default_factory=JobInfo)
    pumps: list = field(default_factory=list)
    analogs: list = field(default_factory=list)
    digitals: list = field(default_factory=list)
    switchgear: list = field(default_factory=list)
    buckets: list = field(default_factory=list)
    ats: list = field(default_factory=list)
    hvac: HVACConfig = field(default_factory=HVACConfig)
    misc: list = field(default_factory=list)
