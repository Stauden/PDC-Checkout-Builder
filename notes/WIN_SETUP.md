# Windows Setup

How to get `make_sheet.py` running on a fresh Windows machine. It renders a Jinja2
HTML template to `sheet.html`, then converts that to a print-ready `sheet.pdf`.

## Verified runtime

This is the exact environment the project was built and confirmed working on:

| Component | Version | Notes |
|---|---|---|
| OS | Windows 11 Pro (10.0.26200) | 64-bit |
| Python | 3.14.3 | `C:\Users\<you>\AppData\Local\Python\pythoncore-3.14-64` (Python Install Manager) |
| pip | 26.2.1 | |
| Jinja2 | 3.1.6 | templating |
| WeasyPrint | 69.0 | HTML to PDF |
| GTK3 Runtime | 3.24.31 | **native, not a pip package — see step 2** |

## Step 1 — Create the virtual environment and install packages

From the project root:

```bat
python -m venv venv
venv\Scripts\activate
pip install jinja2 weasyprint
```

`pip install weasyprint` pulls in its own dependencies automatically
(`pydyf`, `tinycss2`, `tinyhtml5`, `cssselect2`, `pyphen`, `fonttools`,
`cffi`, `pillow`, `brotli`, `zopfli`). You only ever name the two top-level
packages.

> **PowerShell note:** if `venv\Scripts\activate` fails with a script-execution
> error, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, or use
> `venv\Scripts\Activate.ps1`. In `cmd.exe` the plain `activate` always works.

## Step 2 — Install the GTK3 runtime (required, easy to miss)

**This step is not optional and pip will not do it for you.** WeasyPrint renders
text through Pango and GLib, which are C libraries. The pip package ships only
the Python bindings, so a machine without GTK installs cleanly and then crashes
at import time:

```
OSError: cannot load library 'libgobject-2.0-0': error 0x7e.
  Additionally, ctypes.util.find_library() did not manage to locate a library
  called 'libgobject-2.0-0'
```

Install the runtime WeasyPrint's documentation recommends:

```bat
winget install --id tschoonj.GTKForWindows --source winget
```

This installs GTK3 to `C:\Program Files\GTK3-Runtime Win64\bin` and adds that
directory to the **machine** `PATH`. It requires administrator rights, so expect
a UAC prompt.

> **Open a new terminal afterward.** Any terminal that was already running —
> including an integrated VS Code terminal — inherited the old `PATH` and will
> keep throwing the `libgobject-2.0-0` error until it is restarted. This is the
> single most common reason the install "doesn't work."

To confirm the install:

```bat
where libgobject-2.0-0.dll
```

## Step 3 — Run it

```bat
python make_sheet.py
start sheet.pdf
```

Expected output:

```
wrote sheet.html and sheet.pdf
```

## Troubleshooting

**`OSError: cannot load library 'libgobject-2.0-0'`**
GTK is missing, or your terminal predates the install. Do step 2, then open a
new terminal.

**`GLib-GIO-WARNING **: Unexpectedly, UWP app '...' supports 4 extensions but has no verbs`**
Harmless. GLib emits this while scanning Windows file associations. It does not
affect the PDF and can be ignored.

**`UnicodeEncodeError` when writing `sheet.html`**
Windows defaults `open()` to cp1252, which cannot encode every character the
template may contain. The script already passes `encoding="utf-8"` explicitly;
keep that argument if you edit the write call.

## Rebuilding from scratch

If the environment gets into a bad state, delete `venv` and redo step 1. GTK is
installed system-wide and survives — you do not need to repeat step 2.
