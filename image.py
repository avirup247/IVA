from PIL import Image
from PIL import ImageColor , ImageFile

img=Image.open("ui2.png")



fp=open("ui.jpg", "rb")
p = ImageFile.Parser()
i=1
while 1:
    s = fp.read(1024)
    if not s:
        break
    p.feed(s)
    if i <2:
        print(s)

im = p.close()

im.save("copy.jpg")
#img.rotate(45).show()