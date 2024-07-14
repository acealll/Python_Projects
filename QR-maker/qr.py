import qrcode
from PIL import Image

def create_custom_qr(data, logo_path=None, color='black', back_color='white', box_size=10, border=4):
    # a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=back_color)
    img = img.convert("RGB")

    if logo_path:
       
        logo = Image.open(logo_path)
        logo = logo.convert("RGBA")
        box = box_size * 10
        logo.thumbnail((box, box))
        logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        logo_mask = logo.split()[3]
        img.paste(logo, logo_pos, mask=logo_mask)

    return img


data = "https://youtu.be/dQw4w9WgXcQ?si=q2uAGLETiWBu5o4t"
logo_path = "/Users/aceall/Documents/porty/sora.jpg"  
qr_img = create_custom_qr(data, logo_path, color="purple", back_color="white")
qr_img.show()  # one time pop-up of the qr
qr_img.save("custom_qr_code.png")  # saving the image
