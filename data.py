'''
~ per string structure ~
  string_# = { header : value, ..., circuit_strings: [{row_1}, {row_2}, ...],}
'''
PDC_Circuit_Strings = [
  #Circuit #1 - Dictionary
  {
    #String Headers
    "circuit_number": 1,
    "circuit_name": 'CB1 Supply to "A" terminals',
    "drawing_number": "P5033-14",
    "type": "Power",
    #Circuit_String : [ {Row 1 Dict}, {Row 2 Dict}, ... ]
    "circuit_strings": [
      #Element 1 : Row 1
      {
        "device_description": "CB1",
        "input_terminal": "1",
        "comment": "120 VAC control Power",
        "output_terminal": "2",
        "output_wire": "2CLP",
        "logic_gate": "AND"
      },
      #Element 2 : Row 2
      {
        "device_description": "Terminal Strip A Hot Bus",
        "input_terminal": "1",
        "comment": "Verify terminals 1-10 bus jumper",
        "output_terminal": "10",
        "output_wire": "2CLP",
        "logic_gate": "AND"
      },
      #Element 3 : Row 3
      {
        "device_description": "Terminal Strip A Neutral Bus",
        "input_terminal": "19",
        "comment": "Verify terminals 19-24 bus jumper",
        "output_terminal": "24",
        "output_wire": "2CLN",
        "logic_gate": "AND"
      },
      #Element 4 : Row 4
      {
        "device_description": "CB1",
        "input_terminal": "",
        "comment": "Neutral",
        "output_terminal": "4", #ending terminal
        "output_wire": "2CLN", #Wire_#
        "logic_gate": ""
      }
    ]
  },
  #Circuit #2
  {
      #String Headers
      "circuit_number": 2,
      "circuit_name": 'Close & Block Close',
      "drawing_number": "P5033-14",
      "type": "Breaker Close",
      #Circuit_String : [ {Row 1 Dict}, {Row 2 Dict}, ... ]
      "circuit_strings": [
        #Element 1 : Row 1
        {
          "device_description": "Terminal Block A Hot Bus",
          "input_terminal": "N/A",
          "comment": "120 VAC control Power",
          "output_terminal": "2",
          "output_wire": "1CLP",
          "logic_gate": "AND"
        },
        #Element 2 : Row 2
        {
          "device_description": "SEL 700G OUT 102",
          "input_terminal": "A05",
          "comment": "Close Command",
          "output_terminal": "A06",
          "output_wire": "N/A",
          "logic_gate": "AND"
        },
        #Element 3 : Row 3
        {
          "device_description": "Terminal Strip A",
          "input_terminal": "11",
          "comment": "Marshalling Terminals",
          "output_terminal": "11",
          "output_wire": "N/A",
          "logic_gate": "AND"
        },
        #Element 4 : Row 4
        {
          "device_description": "Terminal Strip F",
          "input_terminal": "1",
          "comment": "LV JSR: 86 Permissive",
          "output_terminal": "2",
          "output_wire": "N/A",
          "logic_gate": "AND"
        },
        #Element 5 : Row 5
        {
          "device_description": "Terminal Strip A",
          "input_terminal": "12",
          "comment": "Marshalling Terminals",
          "output_terminal": "12",
          "output_wire": "N/A",
          "logic_gate": "AND"
        },
        #Element 6 : Row 6
        {
          "device_description": "52 MV Breaker",
          "input_terminal": "CD4",
          "comment": "Close Input",
          "output_terminal": "CD14",
          "output_wire": "N/A",
          "logic_gate": "AND"
        },
        #Element 7 : Row 7
        {
          "device_description": "Terminal Strip A Neutral Bus",
          "input_terminal": "",
          "comment": "Neutral",
          "output_terminal": "A19-24", #ending terminal
          "output_wire": "2CLN", #Wire_#
          "logic_gate": ""
        }
      ]
    },
    #Circuit #3
    {
    "circuit_number": 3,
    "circuit_name": "Trip Coil Control",
    "drawing_number": "P5033",
    "type": "Breaker Trip",
    "circuit_strings": [
        # 20
        {"device_description": "Terminal Strip A Hot Bus", "input_terminal": "N/A",
         "comment": "120 VAC control Power", "output_terminal": "A1-10",
         "output_wire": "2CLP", "logic_gate": "AND",
         "color": "", "function_test": ""},
        # 21
        {"device_description": "Section 2 Terminal Strips", "input_terminal": "A3",
         "comment": "LV JSR: XY-1302B Trip", "output_terminal": "F5",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "Salmon", "function_test": "Powered Test: Trip"},
        # 22
        {"device_description": "Terminal Strip A", "input_terminal": "14",
         "comment": "Marshalling Terminals", "output_terminal": "Next Path",
         "output_wire": "N/A", "logic_gate": "OR",
         "color": "", "function_test": ""},
        # 23
        {"device_description": "Section 2 Terminal Strips", "input_terminal": "A3",
         "comment": "LV JSR: SEL-787Z Out 303 Trip", "output_terminal": "F5",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "Salmon", "function_test": "Powered Test: Trip"},
        # 24
        {"device_description": "Terminal Strip A", "input_terminal": "14",
         "comment": "Marshalling Terminals", "output_terminal": "Next Path",
         "output_wire": "N/A", "logic_gate": "OR",
         "color": "", "function_test": ""},
        # 25
        {"device_description": "Terminal Strip A Hot Bus", "input_terminal": "N/A",
         "comment": "120 VAC control Power", "output_terminal": "A1-10",
         "output_wire": "2CLP", "logic_gate": "AND",
         "color": "", "function_test": ""},
        # 26
        {"device_description": "SEL-700G OUT 101", "input_terminal": "A03",
         "comment": "Trip Command", "output_terminal": "A04",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "Green", "function_test": "Powered Test: Trip"},
        # 27
        {"device_description": "Terminal Strip A", "input_terminal": "13",
         "comment": "Marshalling Terminals (bus jumper)", "output_terminal": "14",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "Green", "function_test": ""},
        # 28
        {"device_description": "Terminal Strip CS", "input_terminal": "73",
         "comment": 'S3 (Ground) "b" Contacts (defeats all but 86/PLR trips)',
         "output_terminal": "74",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "", "function_test": "Powered Test: Trip"},
        # 29
        {"device_description": "Terminal Strip A", "input_terminal": "16",
         "comment": "Marshalling Terminals", "output_terminal": "Next Path",
         "output_wire": "N/A", "logic_gate": "OR",
         "color": "", "function_test": ""},
        # 30
        {"device_description": "Terminal Strip A Hot Bus", "input_terminal": "N/A",
         "comment": "120 VAC control Power", "output_terminal": "A1-10",
         "output_wire": "2CLP", "logic_gate": "AND",
         "color": "", "function_test": ""},
        # 31
        {"device_description": "Terminal Strip F", "input_terminal": "3",
         "comment": "LV JSR: 86 LOR Trip", "output_terminal": "4",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "Salmon", "function_test": "Powered Test: Trip"},
        # 32
        {"device_description": "PBO", "input_terminal": "COM",
         "comment": "True unless Open Button is locked out", "output_terminal": "Next Path",
         "output_wire": "N/A", "logic_gate": "OR",
         "color": "", "function_test": ""},
        # 33
        {"device_description": "Terminal Strip A Hot Bus", "input_terminal": "N/A",
         "comment": "120 VAC control Power", "output_terminal": "A1-10",
         "output_wire": "2CLP", "logic_gate": "AND",
         "color": "", "function_test": ""},
        # 34
        {"device_description": "PLR", "input_terminal": "11",
         "comment": "Pressure/Level Relay N.O.", "output_terminal": "7",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "Teal", "function_test": "Powered Test: Trip"},
        # 35
        {"device_description": "PBO", "input_terminal": "COM",
         "comment": "Button pushed defeats 86/PLR trips.", "output_terminal": "NC",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "", "function_test": "Powered Test: Trip"},
        # 36
        {"device_description": "Terminal Strip A", "input_terminal": "15",
         "comment": "Marshalling Terminals (bus jumper)", "output_terminal": "16",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "", "function_test": ""},
        # 37
        {"device_description": "52 MV Breaker", "input_terminal": "CD31",
         "comment": "Trip Input", "output_terminal": "CD30",
         "output_wire": "N/A", "logic_gate": "AND",
         "color": "", "function_test": ""},
        # 38 - ending: output_wire is the Wire #, output_terminal the Ending Terminal
        {"device_description": "Terminal Strip A Neutral Bus", "input_terminal": "",
         "comment": "Neutral", "output_terminal": "A19-24",
         "output_wire": "2CLN", "logic_gate": "",
         "color": "", "function_test": ""},
    ],
}
]