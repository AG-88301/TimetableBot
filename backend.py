from PIL import Image, ImageDraw, ImageFont

import numpy as np

class Timetable:
    def __init__(self):
        pass
    
    def get_timetable(self, img: str) -> str:
        pass

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
        font = ImageFont.truetype("Arial.ttf", 15)
        draw = ImageDraw.Draw(base)
        
        pos = [
            [(140, 75), (215, 75), (290, 75), (365, 75), (440, 75)],
            [(140, 105), (215, 105), (290, 105), (365, 105), (440, 105)],
            [(140, 140), (215, 140), (290, 140), (365, 140), (440, 140)],
            [(140, 170), (215, 170), (290, 170), (365, 170), (440, 170)],
            [(140, 203), (215, 203), (290, 203), (365, 203), (440, 203)],
    
            [(140, 310), (215, 310), (290, 310), (365, 310), (440, 310)],
            [(140, 345), (215, 345), (290, 345), (365, 345), (440, 345)],
            [(140, 380), (215, 380), (290, 380), (365, 380), (440, 380)],
            [(140, 410), (215, 410), (290, 410), (365, 410), (440, 410)],
            [(140, 445), (215, 445), (290, 445), (365, 445), (440, 445)]
        ]
        
        for r_ind, row in enumerate(ttbl):
            for c_ind, col in enumerate(row):
                draw.text(pos[r_ind][c_ind], col, fill=font_color, font=font)

        return base
        
    def add_mask(self, im: Image, rgb: tuple) -> Image:
        im.convert('RGBA')
        data = np.array(im)
        r, g, b, a = data.T
        
        col = np.logical_not(a == 0)
        data[..., :-1][col.T] = rgb
        
        im = Image.fromarray(data)
        return im
        
if __name__ == "__main__":
    ttbl = Timetable()
    ttbl.get_timetable("IMG_1648.jpg")