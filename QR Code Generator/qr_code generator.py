import qrcode
url = input("Enter the URL:").strip()
file_path = "C:\\Users\\Sonalirams\\OneDrive\\Desktop\\qrcode.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file_path)

print("The QRCode was successfully generated")
