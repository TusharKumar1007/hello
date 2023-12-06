import qrcode

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5,
)

qr.add_data("Hello this is a Qr!")

qr.make(fit=True)

img=qr.make_image(fill_color='lime',back_color='black')

img.save('Qrcode.png')