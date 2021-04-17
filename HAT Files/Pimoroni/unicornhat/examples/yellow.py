import unicornhat as unicorn

#setup unicorn hat
unicorn.set_layout(unicorn.AUTO)
unicorn.brightness(0.5)

#get width and height
width, height = unicorn.get_shape()

r=255
g=177
b=0

def setcol():
        for y in range(height):
                for x in range(width):
                        unicorn.set_pixel(x,y,r,g,b)
                        unicorn.show()

while True:
        setcol()





