from pathlib import Path
from jinja2 import Template

'''
~ per string structure ~
string_# = { header: value..., circuit_strings: [row_1, row_2, ...]}
'''
string_1 = {
    #String Headers
    "circuit_number": 1,
    "circuit_name": 'CB1 Supply to "A" terminals',
    "drawing_number": "P5033",
    "type": "Power",

    #Circuit String
    "circuit_strings": [
        {"device_description": "CB1",
         "input_terminal": "1",
         "comment": "120 VAC control Power",
         "output_terminal": "2",
         "output_wire": "2CLP",
         "logic_gate": "AND"},

        {"device_description": "Terminal Strip A Hot Bus",
         "input_terminal": "1",
         "comment": "Verify terminals 1-10 bus jumper",
         "output_terminal": "10",
         "output_wire": "2CLP",
         "logic_gate": "AND"},
         
        {"device_description": "Terminal Strip A Neutral Bus",
         "input_terminal": "19",
         "comment": "Verify terminals 19-24 bus jumper",
         "output_terminal": "24",
         "output_wire": "2CLN",
         "logic_gate": "AND"},

        {"device_description": "CB1",
         "input_terminal": "",
         "comment": "Neutral",
         "output_terminal": "4",
         "output_wire": "2CLN",
         "logic_gate": "END"},
    ]
}

TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8">
<style>
  @page { size: letter landscape; margin: 0.5in; }
  body { font-family: Calibri, Arial, sans-serif; font-size: 11pt; }
  table { border-collapse: collapse; width: 100%; }
  td { border: 1px solid #000; padding: 2px 6px; }
  .outer { border: 2px solid #000; }
  .shade { background: #d9d9d9; }
  .title { text-align: center; font-weight: bold; }
  .label { text-align: right; }
  .value { text-align: center; font-weight: bold; }
  .desc  { text-align: center; }
  .fieldname { font-style: italic; font-size: 10pt; }
  .idx { text-align: right; font-style: italic; vertical-align: bottom; }
  .initials { width: 9%; }
  .notes { text-align: center; }
  .noteline { height: 22px; }
  .blockend td, td.blockend { border-bottom: 2px solid #000; }
</style></head>
<body>
<table class="outer">
 
  <tr>
    <td class="label">Initials:</td>
    <td class="title" colspan="3">Switch Gear Circuit #{{ circuit_number }}</td>
  </tr>
 
  <tr>
    <td class="shade blockend" rowspan="3"></td>
    <td class="label">Circuit Name:</td>
    <td class="desc" colspan="2">{{ circuit_name }}</td>
  </tr>
  <tr>
    <td class="label">Drawing Number:</td>
    <td class="desc" colspan="2">{{ drawing_number }}</td>
  </tr>
  <tr>
    <td class="label">Type:</td>
    <td class="desc" colspan="2">{{ type }}</td>
  </tr>
 
  {% for r in circuit_strings %}
    {% if r.logic_gate == "END" %}
      <tr>
        <td class="initials"></td>
        <td class="desc">{{ r.device_description }}</td>
        <td class="value">{{ r.output_wire }}</td>
        <td class="fieldname">Wire #</td>
      </tr>
      <tr class="blockend">
        <td class="shade idx">{{ loop.index }}</td>
        <td class="desc">{{ r.comment }}</td>
        <td class="value">{{ r.output_terminal }}</td>
        <td class="fieldname">Ending Terminal</td>
      </tr>
    {% else %}
      <tr>
        <td class="initials"></td>
        <td class="desc">{{ r.device_description }}</td>
        <td class="value">{{ r.input_terminal }}</td>
        <td class="fieldname">Input Terminal</td>
      </tr>
      <tr>
        <td class="shade idx blockend" rowspan="3">{{ loop.index }}</td>
        <td class="desc">{{ r.comment }}</td>
        <td class="value">{{ r.output_terminal }}</td>
        <td class="fieldname">Output Terminal</td>
      </tr>
      <tr>
        <td></td>
        <td class="value">{{ r.output_wire }}</td>
        <td class="fieldname">Output Wire #</td>
      </tr>
      <tr class="blockend">
        <td></td>
        <td class="value">{{ r.logic_gate }}</td>
        <td class="fieldname">Logic</td>
      </tr>
    {% endif %}
  {% endfor %}
 
  <tr>
    <td class="shade"></td>
    <td class="notes">Notes</td>
    <td class="shade" colspan="2"></td>
  </tr>
  <tr><td class="noteline" colspan="4"></td></tr>
  <tr><td class="noteline" colspan="4"></td></tr>
 
</table>
</body></html>
"""
 
html = Template(TEMPLATE).render(**string_1)
Path("sheet.html").write_text(html, encoding="utf-8")
 
from weasyprint import HTML
HTML(string=html).write_pdf("sheet.pdf")
print("wrote sheet.html and sheet.pdf")

