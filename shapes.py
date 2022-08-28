import svgwrite
from svgwrite import cm, mm
from PIL import Image, ImageOps, ImageDraw, ImageFont


shape = '''\
##\
'''

shape = '''\
##
#
##\
'''

shape = '''\
###
 #
 #\
'''
U = 200# * mm # base unit

def pil_draw_shape(shape, fish, time, earned_fish):
    fish_img = ImageOps.fit(Image.open("fish.png"), (U,U))
    text = f"🐟{fish}\n⌛{time}"
    shape = shape.splitlines()
    X = max([len(line) for line in shape])
    Y = len(shape)
    out = Image.new('1', (X*U, Y*U), 0)
    d = ImageDraw.Draw(out)
    first = True
    earned_fish_coords = []
    for i, line in enumerate(shape):
        for j, char in enumerate(line):
            if not char.isspace():
                y = i*U
                x = j*U
                d.rectangle([(x,y), (x+U,y+U)], fill=1)
                if first:
                    text_coords = (x+0.1*U,y+ 0.1*U)
                    first = False
                elif earned_fish > 0:
                    earned_fish_coords += [(x,y)]
                    earned_fish -= 1
                    print(earned_fish)

    img = ImageOps.fit(Image.open('coral1.jpg'),out.size)
    img.putalpha(out)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("./NotoEmoji-Medium.ttf", 60)
    d.text(text_coords, text, font=fnt, fill=(0,0,0))
    print(earned_fish_coords)
    for coord in earned_fish_coords:
        img.paste(fish_img, coord, fish_img)
    img.show()



if __name__ == "__main__":
    pil_draw_shape(shape, 6, 2, 2)


