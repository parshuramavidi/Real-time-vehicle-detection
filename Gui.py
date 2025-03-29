import tkinter as tk
from tkinter import filedialog
from tkinter import *  
import os
import subprocess
import numpy 
 
#initialise GUI
top=tk.Tk()
top.geometry('1200x750')
top.title('Object Detection, Vehicle Counting and Classification Sytem')
bg = PhotoImage(file = "a.png")
canvas1 = Canvas( top, width = 800, height = 800)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")



# top.configure(background= bg)

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path): 
    # print(file_path)
    Str="Main1.py --input inputVideos/PexelsVideos1721294.mp4 --output outputVideos/PexelsVideos1721294.avi --yolo yolo-"
    # harActivity = "Main1.py --input inputVideos/bridge.mp4 --output outputVideos/bridgeOut.avi --yolo yolo-"
    subprocess.call("python "+Str)
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Get RealTime Reading",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
    button2_canvas = canvas1.create_window( 800, 300, anchor = "nw", window = classify_b)

def upload_video():
    try:
        file_path=filedialog.askopenfilename() 
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload=Button(top,text="Upload Input Video",command=upload_video,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
button1_canvas = canvas1.create_window( 300, 500, anchor = "nw", window = upload)

sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Object Detection, Vehicle Counting and Classification Sytem",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#FF0000')
heading.pack()
button2_canvas = canvas1.create_window( 100, 100, anchor = "nw", window = heading)

top.mainloop()
