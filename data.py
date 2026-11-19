"""
Switch gear circuit strings from the 4396 G0101 GIS Tech Checkout sheet
(scanned copy, pages 2-26): Switch Gear Circuits #1-#49, elements 1-200.

~ per string structure ~
  string_# = { header : value, ..., circuit_strings: [{row_1}, {row_2}, ...],}

Element comments (# 20) are the element numbers printed on the sheet.
Ending rows: output_wire is the Wire #, output_terminal the Ending Terminal.
color is the colour tag in the left column; function_test is the text
printed in the Logic row (e.g. "Powered Test: Other Test").
"""
PDC_Circuit_Strings = [
  # Circuit #1
  {
    "circuit_number": 1,
    "circuit_name": 'CB1 Supply to "A" terminals',
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 1
      {
        "device_description": "CB1",
        "input_terminal": "1",
        "comment": "120 VAC control Power",
        "output_terminal": "2",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 2
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "1",
        "comment": "Verify terminals 1-10 bus jumper",
        "output_terminal": "10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 3
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "19",
        "comment": "Verify terminals 19-24 bus jumper",
        "output_terminal": "24",
        "output_wire": "2CLN",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 4 - ending
      {
        "device_description": "CB1",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "4",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #2
  {
    "circuit_number": 2,
    "circuit_name": "Close & Block Close",
    "drawing_number": "P5033",
    "type": "Breaker Close",
    "circuit_strings": [
      # 5
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 6
      {
        "device_description": "SEL-700G OUT 102",
        "input_terminal": "A05",
        "comment": "Close Command",
        "output_terminal": "A06",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Close Command"
      },
      # 7
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "11",
        "comment": "Marshalling Terminals",
        "output_terminal": "11",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 8
      {
        "device_description": "Terminal Strip F",
        "input_terminal": "1",
        "comment": "LV JSR: 86 Permissive",
        "output_terminal": "2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Salmon",
        "function_test": "Powered Test: Close Command"
      },
      # 9
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "12",
        "comment": "Marshalling Terminals",
        "output_terminal": "12",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 10
      {
        "device_description": "52 MV Breaker",
        "input_terminal": "CD4",
        "comment": "Close Input",
        "output_terminal": "CD14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 11 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #3
  {
    "circuit_number": 3,
    "circuit_name": "Breaker Open Lamp",
    "drawing_number": "P5033",
    "type": "Lamp",
    "circuit_strings": [
      # 12
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 13
      {
        "device_description": "Breaker Open Lamp",
        "input_terminal": "X1",
        "comment": "Green Lamp",
        "output_terminal": "X2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 14
      {
        "device_description": "52 MV Breaker",
        "input_terminal": "CD28",
        "comment": '"b" Aux Contacts',
        "output_terminal": "CD38",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 15 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #4
  {
    "circuit_number": 4,
    "circuit_name": "Breaker Closed Lamp",
    "drawing_number": "P5033",
    "type": "Lamp",
    "circuit_strings": [
      # 16
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 17
      {
        "device_description": "Breaker Closed Lamp",
        "input_terminal": "X1",
        "comment": "Red Lamp",
        "output_terminal": "X2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 18
      {
        "device_description": "52 MV Breaker",
        "input_terminal": "CD9",
        "comment": '"a" Aux Contacts',
        "output_terminal": "CD19",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 19 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #5
  {
    "circuit_number": 5,
    "circuit_name": "Trip Coil Control",
    "drawing_number": "P5033",
    "type": "Breaker Trip",
    "circuit_strings": [
      # 20
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 21
      {
        "device_description": "Section 2 Terminal Strips",
        "input_terminal": "A3",
        "comment": "LV JSR: XY-1302B Trip",
        "output_terminal": "F5",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Salmon",
        "function_test": "Powered Test: Trip"
      },
      # 22
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "14",
        "comment": "Marshalling Terminals",
        "output_terminal": "Next Path",
        "output_wire": "N/A",
        "logic_gate": "OR",
        "color": "",
        "function_test": ""
      },
      # 23
      {
        "device_description": "Section 2 Terminal Strips",
        "input_terminal": "A3",
        "comment": "LV JSR: SEL-787Z Out 303 Trip",
        "output_terminal": "F5",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Salmon",
        "function_test": "Powered Test: Trip"
      },
      # 24
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "14",
        "comment": "Marshalling Terminals",
        "output_terminal": "Next Path",
        "output_wire": "N/A",
        "logic_gate": "OR",
        "color": "",
        "function_test": ""
      },
      # 25
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 26
      {
        "device_description": "SEL-700G OUT 101",
        "input_terminal": "A03",
        "comment": "Trip Command",
        "output_terminal": "A04",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Green",
        "function_test": "Powered Test: Trip"
      },
      # 27
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "13",
        "comment": "Marshalling Terminals (bus jumper)",
        "output_terminal": "14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Green",
        "function_test": ""
      },
      # 28
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "73",
        "comment": 'S3 (Ground) "b" Contacts (defeats all but 86/PLR trips)',
        "output_terminal": "74",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Trip"
      },
      # 29
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "16",
        "comment": "Marshalling Terminals",
        "output_terminal": "Next Path",
        "output_wire": "N/A",
        "logic_gate": "OR",
        "color": "",
        "function_test": ""
      },
      # 30
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 31
      {
        "device_description": "Terminal Strip F",
        "input_terminal": "3",
        "comment": "LV JSR: 86 LOR Trip",
        "output_terminal": "4",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Salmon",
        "function_test": "Powered Test: Trip"
      },
      # 32
      {
        "device_description": "PBO",
        "input_terminal": "COM",
        "comment": "True unless Open Button is locked out",
        "output_terminal": "Next Path",
        "output_wire": "N/A",
        "logic_gate": "OR",
        "color": "",
        "function_test": ""
      },
      # 33
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 34
      {
        "device_description": "PLR",
        "input_terminal": "11",
        "comment": "Pressure/Level Relay N.O.",
        "output_terminal": "7",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Teal",
        "function_test": "Powered Test: Trip"
      },
      # 35
      {
        "device_description": "PBO",
        "input_terminal": "COM",
        "comment": "Button pushed defeats 86/PLR trips.",
        "output_terminal": "NC",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Trip"
      },
      # 36
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "15",
        "comment": "Marshalling Terminals (bus jumper)",
        "output_terminal": "16",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 37
      {
        "device_description": "52 MV Breaker",
        "input_terminal": "CD31",
        "comment": "Trip Input",
        "output_terminal": "CD30",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 38 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #6
  {
    "circuit_number": 6,
    "circuit_name": "Trip Coil Monitor",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 39
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 40
      {
        "device_description": "SEL-700G IN 408",
        "input_terminal": "D15",
        "comment": "Trip Coil Health",
        "output_terminal": "D16",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Black",
        "function_test": "Powered Test: Other Test"
      },
      # 41
      {
        "device_description": "52 MV Breaker Coil Health Terminal",
        "input_terminal": "CD32",
        "comment": "Path Through Trip Coil",
        "output_terminal": "CD30",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 42 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #7
  {
    "circuit_number": 7,
    "circuit_name": "AC to DC Rectifier",
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 43
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 44
      {
        "device_description": "Terminal Strip CD",
        "input_terminal": "23",
        "comment": 'QF "b" Contacts',
        "output_terminal": "33",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 45
      {
        "device_description": "DSN",
        "input_terminal": "CS1",
        "comment": "3 Pos Sw Man Op Elect Interlock",
        "output_terminal": "CS2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Black",
        "function_test": ""
      },
      # 46 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #8
  {
    "circuit_number": 8,
    "circuit_name": "Spring Charge Motor Control",
    "drawing_number": "P5033",
    "type": "Permissive",
    "circuit_strings": [
      # 47
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 48
      {
        "device_description": "MCC",
        "input_terminal": "9",
        "comment": "Motor Charge Control Relay",
        "output_terminal": "5",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Black",
        "function_test": ""
      },
      # 49
      {
        "device_description": "MV1",
        "input_terminal": "CD25",
        "comment": "Spring Charge Motor",
        "output_terminal": "CD35",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 50 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #9
  {
    "circuit_number": 9,
    "circuit_name": "Breaker Trip Permissive",
    "drawing_number": "P5033",
    "type": "Breaker Trip",
    "circuit_strings": [
      # 51
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 52
      {
        "device_description": "Terminal Strip CD",
        "input_terminal": "5",
        "comment": 'QF "a" Contacts',
        "output_terminal": "15",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 53
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "45",
        "comment": 'S3 Ground "a" Contacts',
        "output_terminal": "46",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 54
      {
        "device_description": "V2 - Block Trip Magnet (BTM)",
        "input_terminal": "CS46",
        "comment": "Electro-Mechanical Interlock",
        "output_terminal": "A23",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 55 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #10
  {
    "circuit_number": 10,
    "circuit_name": "Safety Interlock",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 56
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 57
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "13",
        "comment": 'S1 Close "a" Contacts',
        "output_terminal": "14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 58
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "26",
        "comment": "Marshalling Terminals",
        "output_terminal": "26",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 59
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "25",
        "comment": "Marshalling Terminals",
        "output_terminal": "Next Path",
        "output_wire": "N/A",
        "logic_gate": "OR",
        "color": "",
        "function_test": ""
      },
      # 60
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 61
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "27",
        "comment": 'S2 Open "a" Contacts',
        "output_terminal": "28",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Red",
        "function_test": ""
      },
      # 62
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "26-25",
        "comment": "Marshalling Terminals (bus jumper)",
        "output_terminal": "Next Path",
        "output_wire": "N/A",
        "logic_gate": "OR",
        "color": "",
        "function_test": ""
      },
      # 63
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 64
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "43",
        "comment": 'S3 Ground "a" Contacts',
        "output_terminal": "44",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Green",
        "function_test": ""
      },
      # 65
      {
        "device_description": "VDR",
        "input_terminal": "12",
        "comment": "Voltage Detection Relay (N.O.)",
        "output_terminal": "8",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Green",
        "function_test": ""
      },
      # 66
      {
        "device_description": "Terminal Strip A",
        "input_terminal": "25",
        "comment": "Marshalling Terminals",
        "output_terminal": "25",
        "output_wire": "BKRIN1",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 67
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "59",
        "comment": 'S8 Man/Elect Aux Sw "b" Contacts',
        "output_terminal": "60",
        "output_wire": "BKRIN2",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 68
      {
        "device_description": "U2 PLR",
        "input_terminal": "10",
        "comment": "Pressure Level Relay (N.C.)",
        "output_terminal": "2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 69
      {
        "device_description": "Terminal Strip CD",
        "input_terminal": "10",
        "comment": 'QF "b" Contacts/ Y1 CB Close Interlock',
        "output_terminal": "20",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 70 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #11
  {
    "circuit_number": 11,
    "circuit_name": "Switch Close Lamp",
    "drawing_number": "P5033",
    "type": "Lamp",
    "circuit_strings": [
      # 71
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 72
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "7",
        "comment": 'S1 Close "a" Contacts',
        "output_terminal": "8",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 73
      {
        "device_description": "Switch Closed Lamp",
        "input_terminal": "X1",
        "comment": "Red Lamp",
        "output_terminal": "X2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 74 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #12
  {
    "circuit_number": 12,
    "circuit_name": "Switch Open Lamp",
    "drawing_number": "P5033",
    "type": "Lamp",
    "circuit_strings": [
      # 75
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 76
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "21",
        "comment": 'S2 Open "a" Contacts',
        "output_terminal": "22",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 77
      {
        "device_description": "Switch Open Lamp",
        "input_terminal": "X1",
        "comment": "Green Lamp",
        "output_terminal": "X2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 78 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #13
  {
    "circuit_number": 13,
    "circuit_name": "Switch Ground Lamp",
    "drawing_number": "P5033",
    "type": "Lamp",
    "circuit_strings": [
      # 79
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "A1-10",
        "output_wire": "2CLP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 80
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "37",
        "comment": 'S3 Ground "a" Contacts',
        "output_terminal": "38",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 81
      {
        "device_description": "Switch Ground Lamp",
        "input_terminal": "X1",
        "comment": "Yellow Lamp",
        "output_terminal": "X2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 82 - ending
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "A19-24",
        "output_wire": "2CLN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #14
  {
    "circuit_number": 14,
    "circuit_name": 'CB2 Supply to "B" terminals',
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 83
      {
        "device_description": "CB2",
        "input_terminal": "1",
        "comment": "120 VAC Control Power",
        "output_terminal": "2",
        "output_wire": "2TPMCP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 84
      {
        "device_description": "Terminal Strip B Hot Bus",
        "input_terminal": "1",
        "comment": "Verify terminals 1-3 bus jumper",
        "output_terminal": "3",
        "output_wire": "2TPMCP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 85
      {
        "device_description": "Terminal Strip B Neutral Bus",
        "input_terminal": "4",
        "comment": "Verify terminals 4-6 bus jumper",
        "output_terminal": "5",
        "output_wire": "2TPMCN",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 86 - ending
      {
        "device_description": "CB2",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "4",
        "output_wire": "2TPMCN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #15
  {
    "circuit_number": 15,
    "circuit_name": "Power to CVD10",
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 87
      {
        "device_description": "Terminal Strip B Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "B1-3",
        "output_wire": "2TPMCP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 88
      {
        "device_description": "CVD10",
        "input_terminal": "1",
        "comment": "Voltage Detection System",
        "output_terminal": "2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 89 - ending
      {
        "device_description": "Terminal Strip B Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "B4-6",
        "output_wire": "2TPMCN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #16
  {
    "circuit_number": 16,
    "circuit_name": "Power to TPMC",
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 90
      {
        "device_description": "Terminal Strip B Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "B1-3",
        "output_wire": "2TPMCP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 91
      {
        "device_description": "TPMC",
        "input_terminal": "1",
        "comment": "Three Position Motor Controller",
        "output_terminal": "2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 92 - ending
      {
        "device_description": "Terminal Strip B Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "B4-6",
        "output_wire": "2TPMCN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #17
  {
    "circuit_number": 17,
    "circuit_name": "Power to M2",
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 93
      {
        "device_description": "TPMC",
        "input_terminal": "N/A",
        "comment": "TPMC Motor Power",
        "output_terminal": "3",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 94
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "49",
        "comment": "Three Position Switch Motor (R)+, (BL)-",
        "output_terminal": "50",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 95 - ending
      {
        "device_description": "TPMC",
        "input_terminal": "",
        "comment": "TPMC Motor Power",
        "output_terminal": "4",
        "output_wire": "N/A",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #18
  {
    "circuit_number": 18,
    "circuit_name": "TPMC Commom Bus",
    "drawing_number": "P5033",
    "type": "Input",
    "circuit_strings": [
      # 96
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Common for Inputs",
        "output_terminal": "24",
        "output_wire": "2TPMC1",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 97 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Verify terminals 7-13 bus jumper",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #19
  {
    "circuit_number": 19,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 98
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Alarm Reset",
        "output_terminal": "10",
        "output_wire": "2TPMC AR",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 99
      {
        "device_description": "SEL-700G OUT 301",
        "input_terminal": "C02",
        "comment": "Alarm Reset",
        "output_terminal": "C01",
        "output_wire": "2TPMC1",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 100 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #20
  {
    "circuit_number": 20,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 101
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "VCB Interlocking",
        "output_terminal": "11",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 102
      {
        "device_description": "Terminal Strip CD",
        "input_terminal": "18",
        "comment": 'QF "b" Contacts',
        "output_terminal": "8",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 103 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #21
  {
    "circuit_number": 21,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 104
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Electrically Operated",
        "output_terminal": "12",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 105
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "58",
        "comment": 'S8 Man/Elect Aux Sw "b" Contacts',
        "output_terminal": "57",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 106 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #22
  {
    "circuit_number": 22,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 107
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Switch Close (from Open)",
        "output_terminal": "13",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 108
      {
        "device_description": "PCL",
        "input_terminal": "NC",
        "comment": "Prevent Close Lock (N.C.)",
        "output_terminal": "COM",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 109
      {
        "device_description": "Red PB",
        "input_terminal": "24",
        "comment": "Close Push Button",
        "output_terminal": "23",
        "output_wire": "2TPMC1",
        "logic_gate": "AND",
        "color": "Black",
        "function_test": ""
      },
      # 110 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #23
  {
    "circuit_number": 23,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 111
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Switch Open (from Closed)",
        "output_terminal": "14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 112
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "6",
        "comment": 'S1 Close "a" Contacts',
        "output_terminal": "5",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 113
      {
        "device_description": "Green PB",
        "input_terminal": "24",
        "comment": "Open Push Button",
        "output_terminal": "23",
        "output_wire": "2TPMC1",
        "logic_gate": "AND",
        "color": "Black",
        "function_test": ""
      },
      # 114 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #24
  {
    "circuit_number": 24,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 115
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Switch Ground (from Open)",
        "output_terminal": "15",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 116
      {
        "device_description": "PG",
        "input_terminal": "NC",
        "comment": "Prevent Grounding (N.C.)",
        "output_terminal": "COM",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 117
      {
        "device_description": "VDR",
        "input_terminal": "6",
        "comment": "Voltage Detection Relay (N.O.)",
        "output_terminal": "10",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 118
      {
        "device_description": "White PB",
        "input_terminal": "24",
        "comment": "Ground Push Button",
        "output_terminal": "23",
        "output_wire": "2TPMC1",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 119 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #25
  {
    "circuit_number": 25,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 120
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Switch Open (from Ground)",
        "output_terminal": "16",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 121
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "36",
        "comment": 'S3 Ground "a" Contacts',
        "output_terminal": "35",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 122
      {
        "device_description": "Green PB",
        "input_terminal": "24",
        "comment": "Open Push Button",
        "output_terminal": "23",
        "output_wire": "2TPMC1",
        "logic_gate": "AND",
        "color": "Black",
        "function_test": ""
      },
      # 123 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #26
  {
    "circuit_number": 26,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 124
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Closing",
        "output_terminal": "17",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 125
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "32",
        "comment": 'S4 Close/Ground Aux "a" Contacts',
        "output_terminal": "31",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 126 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #27
  {
    "circuit_number": 27,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 127
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Opening",
        "output_terminal": "18",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 128
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "18",
        "comment": 'S5 Open to Close Sw "b" Contacts',
        "output_terminal": "17",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 129 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #28
  {
    "circuit_number": 28,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 130
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Opening (2)",
        "output_terminal": "19",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 131
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "48",
        "comment": 'S6 Open Pos. Sw "b" Contacts',
        "output_terminal": "47",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 132 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #29
  {
    "circuit_number": 29,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 133
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Grounding",
        "output_terminal": "20",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 134
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "34",
        "comment": 'S7 Close/Ground Aux Sw "a" Contacts',
        "output_terminal": "33",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 135 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #30
  {
    "circuit_number": 30,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 136
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Closing (2)",
        "output_terminal": "21",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 137
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "10",
        "comment": 'S1 Close "a" Contacts',
        "output_terminal": "9",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 138 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #31
  {
    "circuit_number": 31,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 139
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Opening (3)",
        "output_terminal": "22",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 140
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "24",
        "comment": 'S2 Open "a" Contacts',
        "output_terminal": "23",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 141 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #32
  {
    "circuit_number": 32,
    "circuit_name": "TPMC Input",
    "drawing_number": "P5033",
    "type": "Discrete Input",
    "circuit_strings": [
      # 142
      {
        "device_description": "TPMC Controller",
        "input_terminal": "N/A",
        "comment": "Three Position Grounding (2)",
        "output_terminal": "23",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 143
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "40",
        "comment": 'S3 Ground "a" Contacts',
        "output_terminal": "39",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 144 - ending
      {
        "device_description": "Terminal Strip B Common Bus",
        "input_terminal": "",
        "comment": "Input Common",
        "output_terminal": "B7-13",
        "output_wire": "2TPMC1",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #33
  {
    "circuit_number": 33,
    "circuit_name": 'CB3 Supply to "D" terminals',
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 145
      {
        "device_description": "CB3",
        "input_terminal": "1",
        "comment": "120 VAC Control Power",
        "output_terminal": "2",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 146
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "1",
        "comment": "Verify terminals 1-7 bus jumper",
        "output_terminal": "7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 147
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "8",
        "comment": "Verify terminals 8-12 bus jumper",
        "output_terminal": "12",
        "output_wire": "2SELN",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 148 - ending
      {
        "device_description": "CB3",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "4",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #34
  {
    "circuit_number": 34,
    "circuit_name": "Power to SEL-700G",
    "drawing_number": "P5033",
    "type": "Power",
    "circuit_strings": [
      # 149
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 150
      {
        "device_description": "SEL-700G",
        "input_terminal": "A01",
        "comment": "SEL Power",
        "output_terminal": "A02",
        "output_wire": "2SELN",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 151 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #35
  {
    "circuit_number": 35,
    "circuit_name": "Breaker Closed Status",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 152
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 153
      {
        "device_description": "Terminal Strip CD",
        "input_terminal": "7",
        "comment": 'QF "a" Contacts',
        "output_terminal": "17",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 154
      {
        "device_description": "SEL-700G IN 101",
        "input_terminal": "A10",
        "comment": "Breaker Closed Status",
        "output_terminal": "A11",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 155 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #36
  {
    "circuit_number": 36,
    "circuit_name": "Breaker Open Status",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 156
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 157
      {
        "device_description": "Terminal Strip CD",
        "input_terminal": "29",
        "comment": 'QF "b" Contacts',
        "output_terminal": "39",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 158
      {
        "device_description": "SEL-700G IN 102",
        "input_terminal": "A12",
        "comment": "Breaker Open Status",
        "output_terminal": "A11",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 159 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #37
  {
    "circuit_number": 37,
    "circuit_name": "Switch Ground Indication",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 160
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 161
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "41",
        "comment": 'S3 Ground "a" Contacts',
        "output_terminal": "42",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 162
      {
        "device_description": "SEL-700G IN 401",
        "input_terminal": "D01",
        "comment": "Switch Ground Status",
        "output_terminal": "D02",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 163 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #38
  {
    "circuit_number": 38,
    "circuit_name": "Switch Open Indication",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 164
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 165
      {
        "device_description": "Terminal Strip CS",
        "input_terminal": "29",
        "comment": 'S2 Open "a" Contacts',
        "output_terminal": "30",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 166
      {
        "device_description": "SEL-700G IN 402",
        "input_terminal": "D03",
        "comment": "Switch Open Status",
        "output_terminal": "D04",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 167 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #39
  {
    "circuit_number": 39,
    "circuit_name": "Pressure Level Indication",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 168
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 169
      {
        "device_description": "PLR",
        "input_terminal": "12",
        "comment": "Pressure Level Relay (N.C.)",
        "output_terminal": "4",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 170
      {
        "device_description": "SEL-700G IN 403",
        "input_terminal": "D05",
        "comment": "Pressure Level Status",
        "output_terminal": "D06",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 171 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #40
  {
    "circuit_number": 40,
    "circuit_name": "Autosynch Initiation",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 172
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 173
      {
        "device_description": "Terminal Strip 7D",
        "input_terminal": "4",
        "comment": "LV JSR: Autosynch Init. LVK: 25/26",
        "output_terminal": "13",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Salmon",
        "function_test": ""
      },
      # 174
      {
        "device_description": "SEL-700G IN 404",
        "input_terminal": "D07",
        "comment": "Autosych Command",
        "output_terminal": "D08",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 175 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #41
  {
    "circuit_number": 41,
    "circuit_name": "TPMC Alarm Indication",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 176
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 177
      {
        "device_description": "TPMC Output",
        "input_terminal": "5",
        "comment": "Alarm Status Output",
        "output_terminal": "6",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 178
      {
        "device_description": "SEL-700G IN 405",
        "input_terminal": "D09",
        "comment": "TPMC Alarm Input",
        "output_terminal": "D10",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 179 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #42
  {
    "circuit_number": 42,
    "circuit_name": "TPMC Status Indication",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 180
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 181
      {
        "device_description": "TPMC Output",
        "input_terminal": "7",
        "comment": "Controller Status Output",
        "output_terminal": "8",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 182
      {
        "device_description": "SEL-700G IN 406",
        "input_terminal": "D11",
        "comment": "TPMC Controller Status",
        "output_terminal": "D12",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 183 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #43
  {
    "circuit_number": 43,
    "circuit_name": "PLC Request to Close",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 184
      {
        "device_description": "Terminal Strip D Hot Bus",
        "input_terminal": "N/A",
        "comment": "120 VAC control Power",
        "output_terminal": "D1-7",
        "output_wire": "2SELP",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 185
      {
        "device_description": "Terminal Strip D",
        "input_terminal": "7",
        "comment": "LV JSR: Request to Close from PLC",
        "output_terminal": "14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "Salmon",
        "function_test": ""
      },
      # 186
      {
        "device_description": "SEL-700G IN 407",
        "input_terminal": "D13",
        "comment": "Request to Close from PLC",
        "output_terminal": "D14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      },
      # 187 - ending
      {
        "device_description": "Terminal Strip D Neutral Bus",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "D8-12",
        "output_wire": "2SELN",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #44
  {
    "circuit_number": 44,
    "circuit_name": "SEL-700G OUT 302",
    "drawing_number": "P5033",
    "type": "Placeholder for Function Test",
    "circuit_strings": [
      # 188
      {
        "device_description": "Terminal Strip E",
        "input_terminal": "1",
        "comment": "Raise Gen Speed",
        "output_terminal": "2",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      }
    ]
  },
  # Circuit #45
  {
    "circuit_number": 45,
    "circuit_name": "SEL-700G OUT 303",
    "drawing_number": "P5033",
    "type": "Placeholder for Function Test",
    "circuit_strings": [
      # 189
      {
        "device_description": "Terminal Strip E",
        "input_terminal": "3",
        "comment": "Lower Gen Speed",
        "output_terminal": "4",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      }
    ]
  },
  # Circuit #46
  {
    "circuit_number": 46,
    "circuit_name": "SEL-700G OUT 304",
    "drawing_number": "P5033",
    "type": "Placeholder for Function Test",
    "circuit_strings": [
      # 190
      {
        "device_description": "Terminal Strip E",
        "input_terminal": "5",
        "comment": "Raise Gen Voltage",
        "output_terminal": "6",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      }
    ]
  },
  # Circuit #47
  {
    "circuit_number": 47,
    "circuit_name": "SEL-700G OUT 305",
    "drawing_number": "P5033",
    "type": "Placeholder for Function Test",
    "circuit_strings": [
      # 191
      {
        "device_description": "Terminal Strip E",
        "input_terminal": "7",
        "comment": "Lower Gen Voltage",
        "output_terminal": "8",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": "Powered Test: Other Test"
      }
    ]
  },
  # Circuit #48
  {
    "circuit_number": 48,
    "circuit_name": "VDR Relay",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 192
      {
        "device_description": "C Terminal strip",
        "input_terminal": "3",
        "comment": "120 VAC control power from LV Cabinet",
        "output_terminal": "3",
        "output_wire": "LVACP4",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 193
      {
        "device_description": "CVD10",
        "input_terminal": "4",
        "comment": "Relay 2 N.O.",
        "output_terminal": "5",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 194
      {
        "device_description": "CVD10",
        "input_terminal": "6",
        "comment": "Relay 1 N.C.",
        "output_terminal": "7",
        "output_wire": "VDR2",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 195
      {
        "device_description": "VDR",
        "input_terminal": "13",
        "comment": "Voltage Det. Interlock Relay Coil",
        "output_terminal": "14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 196 - ending
      {
        "device_description": "C Terminal strip",
        "input_terminal": "",
        "comment": "120 VAC neutral from LV",
        "output_terminal": "5",
        "output_wire": "LVACN4",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  },
  # Circuit #49
  {
    "circuit_number": 49,
    "circuit_name": "Pressure Level Relay Relay",
    "drawing_number": "P5033",
    "type": "Status",
    "circuit_strings": [
      # 197
      {
        "device_description": "C Terminal strip",
        "input_terminal": "4",
        "comment": "120 VAC control power from LV Cabinet",
        "output_terminal": "4",
        "output_wire": "LVACP4",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 198
      {
        "device_description": "YL1",
        "input_terminal": "CS53",
        "comment": 'Pressure Meter "a" Contacts',
        "output_terminal": "CS54",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 199
      {
        "device_description": "PLR",
        "input_terminal": "13",
        "comment": "Pressure Level Interlock Relay Coil",
        "output_terminal": "14",
        "output_wire": "N/A",
        "logic_gate": "AND",
        "color": "",
        "function_test": ""
      },
      # 200 - ending
      {
        "device_description": "C Terminal strip",
        "input_terminal": "",
        "comment": "120 VAC neutral from LV",
        "output_terminal": "6",
        "output_wire": "LVACN4",
        "logic_gate": "",
        "color": "",
        "function_test": ""
      }
    ]
  }
]
