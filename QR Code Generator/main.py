import pyqrcode
from pyqrcode import QRCode
s = "https://www.youtube.com/channel/UCwRLqwEjZ_Gk8ztBC59bkiA"
url = pyqrcode.create(s)
url.svg("myyoutube.svg", scale=8)