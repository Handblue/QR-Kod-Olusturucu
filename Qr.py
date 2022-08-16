import pyqrcode

qr = "https://www.google.com/"

url = pyqrcode.create(qr)

url.svg("qrdeneme.svg", scale=10)