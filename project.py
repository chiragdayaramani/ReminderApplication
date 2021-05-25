from tkinter import *
from win10toast import ToastNotifier
import time
from PIL import Image, ImageTk
from threading import Timer
import datetime


class ReminderPage:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap("images/icon.ico")

        self.bg = ImageTk.PhotoImage(file="images/img.jpg")
        self.bg_img = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = Frame(root, height=1200, width=1200, bg="white")
        self.frame.place(x=120, y=100, height=350, width=450)

        self.l1 = Label(self.frame, width=20, text="Title of reminder:")
        self.l2 = Label(self.frame, width=20, text="Message of reminder:")
        self.l3 = Label(self.frame, width=20, text="At Time(HH:MM:SS):")

        self.e1 = Entry(self.frame, width=20, fg="black", bg="white")
        self.e2 = Entry(self.frame, width=20, fg="black", bg="white")
        self.e3 = Entry(self.frame, width=20, fg="black", bg="white")

        self.l4 = Label(self.frame, width=20, font=32, text="MediMinder", bg="white")
        self.l4.place(x=130, y=50)

        self.l1.place(x=100, y=110)
        self.l2.place(x=100, y=150)
        self.l3.place(x=100, y=190)
        self.e1.place(x=270, y=110)
        self.e2.place(x=270, y=150)
        self.e3.place(x=270, y=190)

        self.b1 = Button(self.frame, width=10, height=2, text="OK", command=self.getdata)
        self.b1.place(x=150, y=230)
        self.b2 = Button(self.frame, width=10, height=2, text="Reset", command=self.reset)
        self.b2.place()
        self.b2.place(x=250, y=230)


    def runtoaster(self, *rem_data):
        toaster = ToastNotifier()
        toaster.show_toast(f"{rem_data[0]}",
                           f"{rem_data[1]}",
                           duration=10,
                           threaded=True)
        while toaster.notification_active():
            time.sleep(0.01)

    def getdata(self):
        data_list = ["", "", ""]
        data_list[0] = self.e1.get()
        data_list[1] = self.e2.get()
        data_list[2] = self.e3.get()
        time_min = data_list[2]
        hh, mm, ss = time_min.split(":")
        hh = int(hh)
        mm = int(mm)
        ss = int(ss)
        calltime = hh * 60 * 60 + mm * 60 + ss
        now = datetime.datetime.now()
        hh1 = int(now.hour)
        mm1 = int(now.minute)
        ss1 = int(now.second)
        currtime = hh1 * 60 * 60 + mm1 * 60 + ss1

        timediff = calltime - currtime
        t = Timer(timediff, self.runtoaster, data_list)
        t.start()

    def reset(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)


root = Tk()
root.geometry("1200x1200")

root.title("Reminder App")
l = ReminderPage(root)

root.mainloop()
