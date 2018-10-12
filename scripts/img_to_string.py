import pytesseract
from PIL import Image

img = Image.open(r'E:\福州大学第二十四期本科生科研训练项目申报表格下载\天猫工商信息执照\1.png')
code = pytesseract.image_to_string(img)
print(code)
