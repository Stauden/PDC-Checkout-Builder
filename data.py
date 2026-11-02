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
]