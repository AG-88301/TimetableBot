from email.mime import image
from PIL import Image, ImageDraw, ImageFont
import io

class Timetable:
    def __init__(self):
        pass
    
    def get_timetable(self, img: str) -> str:
        self.img = img


    def expand(self, a: tuple) -> list:
        ttbl = "".join(arg for arg in a)
        ttbl = [row.split(sep=",") for row in ttbl.split(sep="|")]
        return ttbl
        
        
    def compress(self, ttbl: list) -> str:
        new = ""
        for row in ttbl:
            new += "".join((col + ",") for col in row)
            new = new[:-1] + "|"
        return new[:-1]
    
    def table_img(self, ttbl: list) -> Image:
        base = Image.open("base.png")
        font_color = (151, 2, 1)
        font = ImageFont.truetype("Arial.ttf", 20)
        draw = ImageDraw.Draw(base)
        
        pos = [
            [(210, 90), (317, 90), (424, 90), (531, 90), (638, 90)],
            [(210, 135), (317, 135), (424, 135), (531, 135), (638, 135)],
            [(210, 180), (317, 180), (424, 180), (531, 180), (638, 180)],
            [(210, 225), (317, 225), (424, 225), (531, 225), (638, 225)],
            [(210, 270), (317, 270), (424, 270), (531, 270), (638, 270)]
        ]
        
        text = "En"
        draw.text(pos[0][0], text, fill=font_color, font=font)
        
        base.show()
        return base
        
if __name__ == "__main__":
    ttbl = Timetable()
    ttbl.table_img(ttbl=None)