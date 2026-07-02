import qrcode

url = "http://127.0.0.1:5500/qr.html"

img = qrcode.make(url)
img.save("monkey_qr.png")

print("QR code created: monkey_qr.png")
