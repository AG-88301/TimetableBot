from PIL import Image
import cv2
import easyocr
import numpy as np

class Timetable:
    def __init__(self):
        pass
    
    def get_timetable(self, img):
        self.img = img
        image = cv2.imread(self.img)

        reader = easyocr.Reader(['en'],gpu = False) # load once only in memory.
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
        thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        print("wworking")
        r_easy_ocr=reader.readtext(thresh,detail=0)
        print(r_easy_ocr)

    def expand(self, a):
        ttbl = "".join(arg for arg in a)
        ttbl = [row.split(sep=",") for row in ttbl.split(sep="|")]
        return ttbl
        
        
    def compress(self, ttbl):
        new = ""
        for row in ttbl:
            new += "".join((col + ",") for col in row)
            new = new[:-1] + "|"
        return new[:-1]
        
if __name__ == "__main__":
    ttbl = Timetable()
    ttbl.compress([['En', 'Gg', 'Dt', 'Cp', 'Ef'], ['qw', 'er', 'rt', 'yu', 'io'], ['En', 'Gg', 'Dt', 'Cp', 'Ef'], ['En', 'Gg', 'Dt', 'Cp', 'Ef'], ['En', 'Gg', 'Dt', 'Cp', 'Ef']])