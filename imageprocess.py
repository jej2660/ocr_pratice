import pytesseract as pt
import cv2,sys
from PIL import Image

class ImageProcess:
    def __init__(self, path):
        self.orginpath = path
    
    def preProcess(self):
            processed_img = cv2.imread(self.orginpath)
            self.grayscal_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)#gray scale

class OcrProcess:
    def __init__(self, path, lang = "eng"):
        self.grayscal_img = path
        self.lang = lang
    
    def process(self):
            self.textdata = pt.image_to_string(self.grayscal_img, lang=self.lang)

if __name__ == "__main__":
    ip = ImageProcess("./test.png")
    ip.preProcess()
    op = OcrProcess(ip.grayscal_img)
    op.process()
    print(op.textdata)
