import pyautogui as pg
import cv2
import pytesseract as pt
from tkinter import *
import pyperclip

global string

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def screen_shot():
    global text
    pg.screenshot("ss.jpg")
    img = cv2.imread("ss.jpg")
    bbox = cv2.selectROI("Tracking", img, False)
    # xPos, yPos, width, height = cv2.getWindowImageRect("Tracking")
    # if xPos !=-1:
    x, y, w, h = bbox
    img_new = img[y:y+h, x:x+w]
    # cv2.imshow("Frame", img_new)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    try:
        img_new = cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)
        lan = clicked_var.get()
        if lan == "English":
            box = pt.image_to_string(img_new)
        elif lan == "Chinese":
            box = pt.image_to_string(img_new, lang="chi")
        elif lan == "Japanese":
            box = pt.image_to_string(img_new, lang="jpn")
        elif lan == "Korean":
            box = pt.image_to_string(img_new, lang="kor")
        text.delete(1.0, END)
        pyperclip.copy(box)
        text.insert(END, box)
    except:
        pass



win=Tk()
win.geometry("300x233")
# win.resizable(width=False, height=False)
win.iconbitmap("logo.ico")
win.title("Snap Easy")

top_label = Label(win, text="Select the language:")
top_label.place(relx=0.95, anchor=NE)

btn = Button(win, text="Take a shot!", command=screen_shot, height=3, width=20)
btn.pack(pady=3, padx=3, anchor=NW)

clicked_var = StringVar()
clicked_var.set("English")
drop = OptionMenu(win, clicked_var, "Chinese", "English", "Japanese", "Korean")
drop.place(relx=0.9, rely=0.1, anchor=NE)
# # text=""

#
extracted = Label(win, text="Extracted Text")
extracted.pack()
# #
text = Text(win, height=8)
# text.pack()

cancel = Label(win, text="Note:- Press 'c' to cancel")
text.pack()
cancel.pack(anchor=NW)




win.mainloop()
