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

def pil_draw_shape(shape, fish, time, earned_fish, coral_img):
    shape = shape.splitlines()

    X = max([len(line) for line in shape])
    Y = len(shape)

    # Create mask image, empty for now
    out = Image.new('1', (X*U, Y*U), 0)
    # Create an image draw object for adding rectangles and text
    d = ImageDraw.Draw(out)

    # Loop for storing filled coordinates
    first = True
    earned_fish_coords = []
    filled_coords = []
    for i, line in enumerate(shape):
        for j, char in enumerate(line):
            if not char.isspace():
                y = i*U
                x = j*U
                filled_coords += [(x,y)]

    for x, y in filled_coords:
        d.rectangle([(x,y), (x+U,y+U)], fill=1)

    # Select the last filled block for adding text to
    text_x, text_y = filled_coords.pop()
    text_coords = (text_x+0.1*U,text_y+ 0.1*U)

    # Select blocks to add fish picture to
    earned_fish_coords = filled_coords[:earned_fish]

    # Create image of coral that is masked with piece shape
    img = ImageOps.fit(Image.open(coral_img),out.size)
    img.putalpha(out)

    # Write the text to the correct coordinates
    text = f"🐟{fish}\n⌛{time}"
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("./NotoEmoji-Medium.ttf", 60)
    d.text(text_coords, text, font=fnt, fill=(0,0,0))

    # Load the fish image and insert it in correct places
    fish_img = ImageOps.fit(Image.open("fish.png"), (U,U))
    for coord in earned_fish_coords:
        img.paste(fish_img, coord, fish_img)

    img.show()



if __name__ == "__main__":
    pil_draw_shape(shape, 6, 2, 2, 'coral1.jpg')


