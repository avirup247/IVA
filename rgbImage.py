from tkinter import *
from PIL import Image,ImageTk
import req

url="download.jpg"
state=True
root= Tk()
root.geometry('1080x720')
root.title("IVA controlPanel")
root.config(bg="#222222")
img=Image.open(url)
img=img.resize((720,360))
img.convert("RGB")
width,height=img.size

image_label = Label(root)
image_label.grid(row=0,column=0,padx=10, pady=10,rowspan=2)


newImage=ImageTk.PhotoImage(img)
image_label.configure(image=newImage)
image_label.image = newImage

# funtion for filtering
def processImage(image:Image.Image,w:int,h:int):
    image=image.resize((w,h))
    image.convert("RGB")
    filteredImage=Image.new("RGB",(w,h))
    pixels=filteredImage.load()
    for y in range(h):
        print(int(y*100/w))
        for x in range(width):
            r,g,b=image.getpixel((x,y))
            YC=0.2568*r+0.5041*g+0.0979*b+16
            pixels[x,y]=(int(YC),int(YC),int(YC))
    filteredImage=ImageTk.PhotoImage(filteredImage)
    image_label.configure(image=filteredImage)
    image_label.image = filteredImage
#function for startButon
def start_capture():
    global state
    if state :
        captured_image=Image.open(url)#req.load_image()
        if captured_image is not None :
            processImage(captured_image,720,360)
            root.after(2000,start_capture)
    else:
        state=True
def stop_capture():
    global state
    state=False

#configure Button for starting capture
startButton=Button(root,text="START", command=start_capture,bg="#ffffff", width=20, height=4)
startButton.grid(row=0,column=1,padx=20, pady=10)
startButton=Button(root,text="STOP", command=stop_capture,bg="#ffffff", width=20, height=4)
startButton.grid(row=1,column=1,padx=20, pady=10)
root.mainloop()