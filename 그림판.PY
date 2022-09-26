from multiprocessing.connection import wait
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as msg
from tkinter import *
import tkinter
import datetime
from PIL import ImageGrab
from webcolors import rgb_to_name

ps = 'oval'
pencolor = "black"
cvcolor = "white"
btn_cvcolor_fg = "black"
btn_pencolor_fg = "white"
color_change = "pen"
w = 5
win = tkinter.Tk()
window = "ture"
info_text = "사용법\n 그리기 : 왼쪽 마우스 \n 지우기 : 오른쪽 마우스 \n 색 바꾸기 : 버튼 \n 버젼 : 1.0.0"
canvas = Canvas(win, bg=cvcolor, width=600, height=600)

save = 0
win.attributes('-toolwindow', True)

def paint(event) :
    global save, pencolor
    save = 0
    x1, y1 = event.x, event.y
    x2, y2 = x1 + w, y1 + w
    if ps == 'line' :
        canvas.create_line(x1, y1, x2, y2, width=3, fill=pencolor)
    if ps == 'square' :
        canvas.create_rectangle(x1, y1, x2, y2, fill=pencolor, outline=pencolor)
    if ps == 'oval' :
        canvas.create_oval(x1, y1, x2, y2, fill=pencolor, outline=pencolor)

def erase(event) :
    global pencolor
    global cvcolor
    global save
    save = 0
    x1, y1 = event.x, event.y
    x2, y2 = x1 + w, y1 + w
    pencolor = cvcolor
    if ps == 'line' :
        canvas.create_line(x1, y1, x2, y2, width=3, fill=pencolor)
    if ps == 'square' :
        canvas.create_rectangle(x1, y1, x2, y2, fill=pencolor, outline=pencolor)
    if ps == 'oval' :
        canvas.create_oval(x1, y1, x2, y2, fill=pencolor, outline=pencolor)

def change_color_red() :
    global pencolor
    global cvcolor
    global color_change
    global canvas
    if color_change == "pen" :
        pencolor = "red"

    elif color_change == "canvas" :
        cvcolor = "red"
        canvas['bg'] = cvcolor
        
def change_color_green() :
    global pencolor
    global cvcolor
    global color_change
    global canvas
    if color_change == "pen" :
        pencolor = "green"

    elif color_change == "canvas" :
        cvcolor = "green"
        canvas['bg'] = cvcolor

def change_color_blue() :
    global pencolor
    global cvcolor
    global color_change
    global canvas
    if color_change == "pen" :
        pencolor = "blue"
        canvas['bg'] = cvcolor

    elif color_change == "canvas" :
        cvcolor = "blue"
        canvas['bg'] = cvcolor

def change_color_yellow() :
    global pencolor
    global cvcolor
    global color_change
    global canvas
    if color_change == "pen" :
        pencolor = "yellow"
        canvas['bg'] = cvcolor

    elif color_change == "canvas" :
        cvcolor = "yellow"
        canvas['bg'] = cvcolor

def change_color_black() :
    global pencolor
    global cvcolor
    global color_change
    global canvas
    if color_change == "pen" :
        pencolor = "black"
        canvas['bg'] = cvcolor

    elif color_change == "canvas" :
        cvcolor = "black"
        canvas['bg'] = cvcolor

def change_color_white() :
    global pencolor
    global cvcolor
    global color_change
    global canvas
    if color_change == "pen" :
        pencolor = "white"
        canvas['bg'] = cvcolor

    elif color_change == "canvas" :
        cvcolor = "white"
        canvas['bg'] = cvcolor

def custom_color() :
    global pencolor
    msg.showerror("custom color", "this function is not complete.")
    #pencolor = askcolor()
    #print(rgb_to_name(pencolor[0]))

def clear() :
    global canvas
    global save
    save = 1
    canvas.delete(ALL)

def change_thick_plus() :
    global w
    w = w + 5

def change_thick_minus() :
    global w
    w= w - 5

def thick_clear() :
    global w
    w = 5

def get_img() :
    #msg.showerror("ERROR", "this function is not complete.")
    try :
        Files = [('All Files', '*.*'),
            ('PNG Files', '*.png'),
            ('JPG Files', '*.jpg'),
            ('JPEG Files', '*.jpeg'),
            ('ICON Files', '*.ico'),
            ('BMP Files', '*.bmp'),
            ('ROW Files', '*.row'),
            ('TIFF Files', '*.tif')]
        a = askopenfilename(filetypes = Files, defaultextension = Files)
        img = PhotoImage(file = a)
        canvas.create_image(10, 10, anchor=NW, image=img)

    except :
        msg.showerror("get img", "there was an error to get img from your computer.")

def info() :
    global info_
    global window
    global info_text
    if window == "ture" :
        window = "false"
        info_ = Tk()
        info_.title("Info")
        text = Text(info_)
        text.pack()
        text.insert('1.0', info_text)

        def close_window():
            if msg.askyesno("Quit", "Do you want to quit info?"):
                global window
                info_.destroy()
                window = "ture"

        def English() :
            global info_text
            info_text = "Usage\n Draw: Left Mouse \n erase : Right Mouse \n Change Color: Button \n version : 1.0.5 \n made by DJ"

        def Korean() :
            global info_text
            info_text = "사용법\n 그리기 : 왼쪽 마우스 \n 지우기 : 오른쪽 마우스 \n 색 바꾸기 : 버튼 \n 버젼 : 1.0.5"

        def real_time_update_info_text():
            currentTime = datetime.datetime.now()
            info_text[info_text] = currentTime
            info_.after(1, real_time_update_info_text)

        btn_eng = Button(info_, text="English", command=English)
        btn_kr = Button(info_, text="한국어", command=Korean)
        btn_eng.pack()
        btn_kr.pack()
    info_.iconbitmap('icons\info.ico')
    info_.protocol("WM_DELETE_WINDOW", close_window)
    info_.mainloop()


def save():
    global win
    global save
    try :
        msg.showwarning('warning', 'save is works best with Windows version 7.')
        x = win.winfo_rootx()
        y = win.winfo_rooty()
        w = win.winfo_width() + x
        h = win.winfo_height() + y -30
        
        box = (x, y, w, h)
        img=ImageGrab.grab(box)
        Files = [('All Files', '*.*'),
            ('PNG Files', '*.png'),
            ('JPG Files', '*.jpg'),
            ('JPEG Files', '*.jpeg'),
            ('ICON Files', '*.ico'),
            ('BMP Files', '*.bmp'),
            ('ROW Files', '*.row'),
            ('TIFF Files', '*.tif')]
        name = asksaveasfilename(filetypes = Files, defaultextension = Files)
        saveas = name
        img.save(saveas)

        msg.showinfo("Save", "paint is successfully saved.")
        save = 1

    except :
        msg.showerror("Save", "there was an error to save the paint.")

def cv_color() :
    global color_change
    color_change = "canvas"

def pen_color() :
    global color_change
    color_change = "pen"



info_ = ""
win.title("그림판")
def close_paintbrush():
            if save == 0 :
                if msg.askyesno("Save", "paint is not saved. do you stil want to quit?") :
                    win.destroy()
            elif msg.askyesno("Quit", "Do you want to quit paintbrush?"):
                win.destroy()

btn_r = Button(win, text="red", command=change_color_red, bg= "red", fg="white")
btn_g = Button(win, text="green", command=change_color_green, bg="green", fg="white")
btn_b = Button(win, text="blue", command=change_color_blue, bg="blue", fg="white")
btn_y = Button(win, text="yellow", command=change_color_yellow, bg="yellow")
btn_bk = Button(win, text="black", command=change_color_black, bg="black", fg="white")
btn_wt = Button(win, text="white", command=change_color_white, bg="white")
btn_cc = Button(win, text ="custom color", command=custom_color, bg="white", fg="black")
btn_plus = Button(win, text="+", command=change_thick_plus, bg="skyblue")
btn_minus = Button(win, text="-", command=change_thick_minus, bg="skyblue")
btn_thick_clear = Button(win, text="Thick clear", command=thick_clear, bg="skyblue")
btn_clear = Button(win, text="clear", command=clear, bg="white")
btn_info = Button(win, text="Info", command=info, bg = "skyblue", fg = "white")
btn_save = Button(win, text="Save", command=save, bg="skyblue", fg="white")
btn_getimg = Button(win, text = "get img", command=get_img, bg="skyblue", fg="white")
btn_cvcolor = Button(win, text="canvas color", command=cv_color, bg=cvcolor, fg=btn_cvcolor_fg)
btn_pencolor = Button(win, text="pen color", command=pen_color, bg=pencolor, fg=btn_pencolor_fg)

canvas.grid(row=0, column=0, columnspan=16)
btn_pencolor.grid(row=5, column=0)
btn_cvcolor.grid(row=5, column=1)
btn_r.grid(row=5, column=2)
btn_g.grid(row=5, column=3)
btn_b.grid(row=5, column=4)
btn_y.grid(row=5, column=5)
btn_bk.grid(row=5, column=6)
btn_wt.grid(row=5, column=7)
btn_cc.grid(row=5, column=8)
btn_plus.grid(row=5, column=9)
btn_minus.grid(row=5, column=10)
btn_thick_clear.grid(row=5, column=11)
btn_clear.grid(row=5, column=12)
btn_getimg.grid(row=5, column=13)
btn_save.grid(row=5, column=14)
btn_info.grid(row=5, column=15)

win.iconbitmap('icons\icon.ico')
win.protocol("WM_DELETE_WINDOW", close_paintbrush)
win.bind("<B1-Motion>", paint)
win.bind("<B3-Motion>", erase)
win.mainloop()
