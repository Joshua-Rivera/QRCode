# QR Code Generator

A Python Webapp with a Streamlit interface for generating QR code images from URLs or text. Generated images are saved locally in the `qrcodes/` folder.

## Setup

Install Python 3, then open a terminal in the project folder.

Create and activate a virtual environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install streamlit "qrcode[pil]"
```

The app uses Streamlit for the interface, `qrcode` for QR generation, and Pillow for image handling. `pathlib` is part of Python's standard library.

## Run the app

From the project folder, with the virtual environment activated:

```bash
python -m streamlit run strfrontend.py
```

Open the local URL printed in the terminal. To stop the server, press `Ctrl+C` in that terminal.

## Generate a QR code

1. Replace the filename field's `Type here...` text with a name such as `my_website`. Do not include `.png`; the generator appends it automatically.
2. Replace the link field's `Type here...` text with your URL, such as `https://example.com`, or other text to encode.
3. Click **Generate QR Code**.
4. Find the image at `qrcodes/my_website.png`.

The output folder is created automatically. Reusing a filename overwrites the existing image. Files are saved on the machine running Streamlit; the app does not currently provide a browser download button.

## Project structure

```text
QRCODE/
├── .streamlit/
│   └── config.toml      # Streamlit theme settings
├── qrcodes/            # Generated images
├── qr.py               # QR generation functions
├── strfrontend.py      # Streamlit interface
└── README.md
```

## How the code works

`strfrontend.py` collects the filename and link, then calls `make_qr(link, link_name, go)` from `qr.py` when the Generate button is clicked.

- `make_qr(link, link_name, go)` generates and saves `qrcodes/<link_name>.png` when `go` is true. It does not return a value.
- `check_existance(link, link_name, go)` currently generates and attempts to save another image at the supplied filename. Despite its name, it is not an existence check. Changing its local `go` parameter does not change the frontend's variable.

The frontend imports the QR functions and passes user input as arguments. The QR module does not need to import the frontend.

## Theme configuration

Edit `.streamlit/config.toml` to customize the app's appearance. For example:

```toml
[theme]
base = "dark"
primaryColor = "#eb9b61"
backgroundColor = "#d1c8be"
secondaryBackgroundColor = "#b7a494"
textColor = "#000000"
font = "times new roman"
```

Keep `.streamlit/` at the project root, alongside `strfrontend.py`, and launch Streamlit from that directory. Save the configuration and rerun the app to apply changes.

