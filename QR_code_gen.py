"""
Install the needed libraries
create a function that collect the text and converts it to a QR code
save the QR code as an image
run the function
"""
import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="White")
    img.save('qrimg.png')

generate_qrcode('https://www.mann-hummel.com/en/career.html')