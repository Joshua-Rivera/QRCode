import qrcode
from pathlib import Path
output_dir = Path(__file__).parent / "qrcodes"
output_dir.mkdir(parents=True, exist_ok=True)
def make_qr(link, link_name, go):
    if go:
        data = link
        qr = qrcode.QRCode()
        qr.add_data(data)
        qr.make()
        img = qr.make_image()
        output_path = output_dir / link_name
        img.save(f"{output_path}.png")
        print(f"Saved QR code to {output_path}")
def check_existance(link, link_name, go):
    data = link
    output_dir = Path(__file__).parent / "qrcodes"
    output_path = output_dir / link_name
    img = qrcode.make(data)
    if img.save(output_path):
        go = True

