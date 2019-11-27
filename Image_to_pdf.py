import img2pdf 
from PIL import Image 
import os 
imagePath = 'Rain_Girl.jpg'
pdfPath = 'Rain_Girl.pdf'
image = Image.open(imagePath) 
pdfByte = img2pdf.convert(image.filename) 
file = open(pdfPath, 'wb') 
file.write(pdfByte)
file.close() 
image.close() 
print('PDF generated Successfully') 
