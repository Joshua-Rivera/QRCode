import io
import streamlit as st
from PIL import Image
from pathlib import Path
from qr import make_qr, check_existance
go = False
st.title("QR Code Generator")
st.text("Turn a URL into a QR code. Enter a filename and link, then click Generate QR Code to obtain your desired QR.")
link_name = st.text_input("Please enter the desired name of the file:", "")
link = st.text_input("Enter the link to be converted into a QR code:", "")
output_dir = Path(__file__).parent / "qrcodes"
output_path = output_dir / f"{link_name}.png"

if st.button("Generate QR Code"):
    go = True
    make_qr(link, link_name, go)
    if output_path.is_file() and go is True:
        image = Image.open(output_path)
        st.image(image, width=200)
        st.text(f"Your QR Code File can be found at {output_path}, or you can download it here :D")
        st.download_button(
              label="Download PNG",
                data=output_path.read_bytes(),
                file_name=output_path.name,
                mime="image/png",
                on_click="ignore",
            )
        st.success("Successfully Downloaded your QR Code")
        check_existance(link, link_name, go)
        go = False
    elif output_path.is_file() == False and not go:
        st.error("Error, please try again")
    else:
        print(":)") 
