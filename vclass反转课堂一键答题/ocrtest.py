from  PIL import  Image
import pytesseract
image = Image.open('out.jpg')
code = pytesseract.image_to_string(image)
print(code)
