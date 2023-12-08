import qrcode

def qr_create(data: str, color: str, background_color: str):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=background_color)
    img.save("rasm.png")

qr_create("Assalomu alaykum", "red", "blue")