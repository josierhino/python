# QR Code Generator program

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='pink', back_color='white')
    img.save('qrimg.png')

# Asks user for URL and generates QR Code
url = input('Enter your URL: ')
generate_qrcode(url)

# Generates QR code to my LinkedIn! :)
generate_qrcode("https://www.linkedin.com/in/josephine-rhino-9456051ba/")