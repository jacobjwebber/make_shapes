import svgwrite
from svgwrite import cm, mm
from PIL import Image, ImageOps, ImageDraw


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

print(shape)

def draw_shape(shape, name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    shapes = dwg.add(dwg.g(id='shapes'))
    for i, line in enumerate(shape.splitlines()):
        for j, char in enumerate(line):
            if not char.isspace():
                shapes.add(dwg.rect(insert=(j*U, i*U), size=(U, U)))


    dwg.save()

def pil_draw_shape(shape):
    shape = shape.splitlines()
    X = max([len(line) for line in shape])
    Y = len(shape)
    print(X, Y)
    out = Image.new('L', (X*U, Y*U), 0)
    d = ImageDraw.Draw(out)
    for i, line in enumerate(shape):
        for j, char in enumerate(line):
            if not char.isspace():
                x = i*U
                y = j*U
                d.rectangle([(x,y), (x+U,y+U)], fill=100000)
                print(x, y)
    out.show()



if __name__ == "__main__":
    pil_draw_shape(shape)#shape, 'test.svg')
    #mask = Image.open('test.svg').convert('L')


