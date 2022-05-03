import pyqrcode

address = 'https://www.mogicons.com/bg/stickers/love/i-love-you-116/'
url = pyqrcode.create(address)
url.png('Trophies.png', scale=8)


