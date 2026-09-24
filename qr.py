import qrcode
from pathlib import Path
data = "https://linktr.ee/6945s26v4p"
output_dir = Path(__file__).parent / "qrcodes"
output_dir.mkdir(parents=True, exist_ok=True)

img = qrcode.make(data)
output_path = output_dir / "linktree_joshua.png"
img.save(output_path)

print(f"Saved QR code to {output_path}")