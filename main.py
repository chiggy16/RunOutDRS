import tkinter
# from tkinter.constants import ANCHOR, SE
import PIL.Image,PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils
import time


stream = cv2.VideoCapture("clip.mp4")
flag=True
def play(speed): 
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,height=SET_HEIGHT,width=SET_WIDTH)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,26,fill="white",font="Times 26 bold",text="Decision Pending.")
    flag= not flag
    print(f"You clicked on play. {speed}")

def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon=1;
    thread.start()
    print("Player is OUT.")

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("2.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    time.sleep(3)

    frame = cv2.cvtColor(cv2.imread("3.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(2)

    if decision=='out':
        decisionImg = "out.jpg"
    else:
        decisionImg = "notout.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def notout():
    thread = threading.Thread(target=pending, args=("notout",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT.")

# Width and Height of our main screen
SET_WIDTH = 650
SET_HEIGHT=368

# Tkinter GUI
window = tkinter.Tk()
window.title("DRS")
cv_img=cv2.cvtColor(cv2.imread("1.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,height=SET_HEIGHT,width=SET_WIDTH)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()

# Buttons
btn = tkinter.Button(window, text="<< Previous (fast) ",width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (slow) ",width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text=" Next (slow) >>",width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text=" Next (fast) >>",width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text=" Give Out ", width=50,command=out)
btn.pack()
btn = tkinter.Button(window, text=" Give Not Out ",width=50,command=notout)
btn.pack()
window.mainloop()
