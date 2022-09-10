from PIL import Image
import cv2

class Timetable:
    def __init__(self, img):
        self.img = img
    
    def get_timetable(self):
        im = cv2.imread(self.img)
        
        cv2.imshow("Img", im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
    ttbl = Timetable("img.jpg")
    ttbl.get_timetable()