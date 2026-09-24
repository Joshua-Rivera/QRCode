import streamlit as st
from PIL import Image
from pathlib import Path
from qr import make_qr, check_existance
flag = False
go = False
st.title("QR Code Generator")
link_name = st.text_input("Please enter the desired name of the file:", "Type here...")
link = st.text_input("Enter the link to be converted into a QR code:", "Type here...")
output_dir = Path(__file__).parent / "qrcodes"
output_path = output_dir / link_name
if st.button("Generate QR Code"):
    go = True
    make_qr(link, link_name, go)
elif output_path.is_file() and go is True:
    check_existance(link, link_name, go)
    st.success("Success")
    img = Image.open(output_path)
    st.img(img, width=200)
    go = False
elif output_path.is_file() == False and not go:
    st.error("Error, please try again")
else:
    print(":)") 
