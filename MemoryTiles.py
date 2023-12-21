import ctypes
import inspect
import tkinter as tk
import tkinter.font as tkFont
from socket import *
import random, re, time
from threading import *
import threading
from tkinter import messagebox

global win


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global win
        win = self

        icon = tk.PhotoImage(file="res/stop.png")

        self.wm_title("MemoryTiles")

        width = 355
        height = 343
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.iconphoto(False, icon)

        container = tk.Frame(self, height=400, width=600)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, SidePage, Page2, Page3):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        poz1 = tk.PhotoImage(file="res/poz1.png")
        lbl = tk.Label(self, image=poz1)
        lbl.img = poz1
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        play = tk.PhotoImage(file="res/playbutton.png")
        label = tk.Label(image=play)
        label.image = play

        button1 = tk.Button(
            self,
            command=lambda: controller.show_frame(SidePage),
        )
        button1["image"] = play
        button1["justify"] = "center"
        button1["bg"] = "#ebd3f7"
        button1["activebackground"] = "#ffffff"
        button1["relief"] = "flat"
        ft = tkFont.Font(family='Ariel', size=10)
        button1["font"] = ft
        button1.place(x=90, y=140, width=167, height=109)

        label1 = tk.Label(self)
        ft = tkFont.Font(family='Ariel', size=20)
        label1["font"] = ft
        label1["bg"] = "#ebd3f7"
        label1["fg"] = "#000000"
        label1["justify"] = "center"
        label1["text"] = "Welcome to Memory Tiles"
        label1.place(x=7, y=100, width=340, height=30)

class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        play = tk.PhotoImage(file="res/playbutton.png")
        player1 = tk.PhotoImage(file="res/user (1).png")
        player2 = tk.PhotoImage(file="res/user (2).png")
        backi = tk.PhotoImage(file="res/return1.png")
        poz1 = tk.PhotoImage(file="res/poz1.png")

        lbl = tk.Label(self, image=poz1)
        lbl.img = poz1
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        button2 = tk.Button(self)
        button2["bg"] = "#ebd3f7"
        button2["bg"] = "#ebd3f7"
        button2["activebackground"] = "#ffffff"
        ft = tkFont.Font(family='Ariel', size=10)
        label = tk.Label(image=player1)
        label.image = player1
        button2["image"] = player1
        button2["font"] = ft
        button2["fg"] = "#000000"
        button2["justify"] = "center"
        button2["relief"] = "flat"
        button2["text"] = "Button"
        button2["command"] = lambda: controller.show_frame(Page2)

        button3 = tk.Button(self)
        button3["bg"] = "#ebd3f7"
        button3["activebackground"] = "#ffffff"
        ft = tkFont.Font(family='Ariel', size=10)
        label = tk.Label(image=player2)
        label.image = player2
        button3["image"] = player2
        button3["font"] = ft
        button3["fg"] = "#000000"
        button3["justify"] = "center"
        button3["relief"] = "flat"
        button3["text"] = "Button"
        button3["command"] = lambda: controller.show_frame(Page3)

        back = tk.Button(self)
        back["bg"] = "#ebd3f7"
        back["activebackground"] = "#ffffff"
        ft = tkFont.Font(family='Ariel', size=10)
        back["font"] = ft
        back["fg"] = "#000000"
        back["justify"] = "center"
        back["text"] = "Button"
        lb = tk.Label(image=backi)
        lb.image = backi
        back["relief"] = "flat"
        back["image"] = backi
        back["command"] = lambda: controller.show_frame(MainPage)

        back.place(x=290, y=280, width=39, height=42)
        button2.place(x=60, y=120, width=100, height=100)
        button3.place(x=190, y=120, width=100, height=100)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global ip_got
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_got = s.getsockname()[0]
        s.close()

        poz1 = tk.PhotoImage(file="res/poz1.png")

        lbl = tk.Label(self, image=poz1)
        lbl.img = poz1
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        label21 = tk.Label(self)
        ft = tkFont.Font(family='Ariel', size=15)
        label21["font"] = ft
        label21["fg"] = "#000000"
        label21["bg"] = "#ebd3f7"
        label21["justify"] = "center"
        label21["text"] = "Your IP adress is: "

        label22 = tk.Label(self)
        ft = tkFont.Font(family='Ariel', size=24)
        label22["font"] = ft
        label22["fg"] = "#000000"
        label22["bg"] = "#ebd3f7"
        label22["justify"] = "center"
        label22["text"] = ip_got

        label23 = tk.Label(self)
        ft = tkFont.Font(family='Ariel', size=15)
        label23["font"] = ft
        label23["fg"] = "#000000"
        label23["bg"] = "#ebd3f7"
        label23["justify"] = "center"
        label23["text"] = "Tell your friend!"

        back = tk.Button(self)
        back["bg"] = "#ebd3f7"
        back["activebackground"] = "#ffffff"
        ft = tkFont.Font(family='Ariel', size=10)
        back["font"] = ft
        back["fg"] = "#000000"
        back["justify"] = "center"
        back["text"] = "Button"
        backi = tk.PhotoImage(file="res/return1.png")
        lb = tk.Label(image=backi)
        lb.image = backi
        back["image"] = backi
        back["relief"] = "flat"
        back["command"] = lambda: controller.show_frame(SidePage)

        button33 = tk.Button(self)
        setattr(self, "button33", button33)
        button33["bg"] = "#ebd3f7"
        button33["activebackground"] = "#ffffff"
        button33["activeforeground"] = "#836C92"
        ft = tkFont.Font(family='Ariel', size=20)
        button33["font"] = ft
        button33["fg"] = "#000000"
        button33["justify"] = "center"
        button33["text"] = "Ready?"
        button33["relief"] = "flat"
        button33["command"] = self.connect

        label21.place(x=90, y=100, width=175, height=30)
        label22.place(x=75, y=145, width=205, height=25)
        label23.place(x=77, y=190, width=200, height=30)
        back.place(x=290, y=280, width=39, height=42)
        button33.place(x=105, y=240, width=145, height=35)

    def connect(self):
        global win, ip_got
        serverPort = 12000  # isto kao za klijent
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', serverPort))
        images = []
        numb = []
        order = []
        message, clientAddress = serverSocket.recvfrom(2048)
        if (message.decode() == "1"):
            serverSocket.sendto(b"2", clientAddress)
            for i in range(20):
                numb.append(i)
            for i in range(20):
                a = random.randint(0, 19)
                while (numb[a] == -1):
                    a = random.randint(0, 19)
                numb[a] = -1
                order.append(a)
                serverSocket.sendto(a.to_bytes(5, 'little'), clientAddress)
            message, clientAddress = serverSocket.recvfrom(2048)
            if (message.decode() == "3"):
                serverSocket.close()
                windows.destroy(win)
                root2 = tk.Tk()
                pg = Game(root2, order, 1, ip_got)
                root2.mainloop()

class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        setattr(self, "controller", controller)

        poz1 = tk.PhotoImage(file="res/poz1.png")
        lbl = tk.Label(self, image=poz1)
        lbl.img = poz1
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        label31 = tk.Label(self)
        ft = tkFont.Font(family='Ariel', size=15)
        label31["font"] = ft
        label31["fg"] = "#000000"
        label31["bg"] = "#ebd3f7"
        label31["justify"] = "center"
        label31["text"] = "What's your friends IP adress?"

        textBox1 = tk.Entry(self)
        setattr(self, "textBox1", textBox1)
        textBox1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Ariel', size=17)
        textBox1["font"] = ft
        textBox1["fg"] = "#000000"
        textBox1["justify"] = "center"
        textBox1["text"] = "Entry"

        button33 = tk.Button(self)
        setattr(self, "button33", button33)
        button33["bg"] = "#ebd3f7"
        button33["activebackground"] = "#ffffff"
        button33["activeforeground"] = "#836C92"
        ft = tkFont.Font(family='Ariel', size=20)
        button33["font"] = ft
        button33["fg"] = "#000000"
        button33["justify"] = "center"
        button33["text"] = "CONNECT"
        button33["relief"] = "flat"
        button33["command"] = self.button33_command

        back = tk.Button(self)
        back["bg"] = "#ebd3f7"
        back["activebackground"] = "#ffffff"
        ft = tkFont.Font(family='Ariel', size=10)
        back["font"] = ft
        back["fg"] = "#000000"
        back["justify"] = "center"
        back["text"] = "Button"
        backi = tk.PhotoImage(file="res/return1.png")
        lb = tk.Label(image=backi)
        lb.image = backi
        back["image"] = backi
        back["relief"] = "flat"
        back["command"] = self.back

        label31.place(x=27, y=100, width=300, height=42)
        textBox1.place(x=77, y=150, width=200, height=30)
        button33.place(x=108, y=200, width=138, height=30)
        back.place(x=290, y=280, width=39, height=42)

    def button33_command(self):
        global win
        textBox1 = getattr(self, "textBox1")
        ip = textBox1.get()
        root = tk.Toplevel()
        serverName = ip
        serverPort = 12000
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        order = []

        message = b"1"
        clientSocket.sendto(message, (serverName, serverPort))
        response, serverAddress = clientSocket.recvfrom(2048)
        if (response.decode() == "2"):
            for i in range(20):
                response, serverAddress = clientSocket.recvfrom(2048)
                order.append(int.from_bytes(response, 'little'))
        clientSocket.sendto(b"3", (serverName, serverPort))
        clientSocket.close()

        windows.destroy(win)
        root2 = tk.Tk()
        pg = Game(root2, order, 2, ip)
        root2.mainloop()

    def back(self):
        textBox1 = getattr(self, "textBox1")
        controller = getattr(self, "controller")
        controller.show_frame(SidePage)
        textBox1.delete(0)

class Game:
    def __init__(self, root, order, player, ip):
        global r, pl
        pl = player
        r = root
        width = 432
        height = 414
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.protocol('WM_DELETE_WINDOW', self.close_root)

        poz1 = tk.PhotoImage(file="res/poz4.png")
        lbl = tk.Label(root, image=poz1)
        lbl.img = poz1
        lbl.place(relx=0.5, rely=0.5, anchor='center')

        icon = tk.PhotoImage(file="res/stop.png")
        root.iconphoto(False, icon)
        global btn, images, j, cnt1, cnt2, pair, pl1, pl2, label1, label2, square
        global clientAddress, serverPort, serverSocket, serverName, clientSocket
        pair = 10
        cnt1 = 0
        cnt2 = 0
        j = {
            0: 0,
            1: None,  # button j
            12: None,  # button j+1
            2: None,  # image j
            3: 2  # Player 2 uvek igra prvi
        }
        clientAddress = None
        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', serverPort))
        serverName = ip
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        btn = []
        pom = []
        images = []
        ft = tkFont.Font(family='Times', size=10)
        square = tk.PhotoImage(file="res/square.png")
        label = tk.Label(image=square)
        label.image = square
        for i in range(20):
            btn.append(tk.Button(root))
            btn[i]["bg"] = "#ebd3f7"
            btn[i]["font"] = ft
            btn[i]["fg"] = "#000000"
            btn[i]["justify"] = "center"
            btn[i]["text"] = str(i)
            btn[i]["image"] = square
            btn[i]["relief"] = "flat"
            if (player == 1):
                btn[i]["command"] = lambda name=i: self.server(name)
            else:
                btn[i]["command"] = lambda name=i: self.client(name)
        for i in range(10):
            img = tk.PhotoImage(file="res/(" + str(i + 1) + ').png')
            pom.append(img)
            pom.append(img)
        for i in range(20):
            images.append(pom[order[i]])

        def place():
            global pl1, pl2, label1, label2

            ft = tkFont.Font(family='Times', size=10)
            label1["font"] = ft
            label1["fg"] = "#000000"
            label1["bg"] = "#ebd3f7"
            label1["justify"] = "center"
            label1["text"] = "Player 1:"
            label1.place(x=20, y=50, width=70, height=25)

            ft = tkFont.Font(family='Times', size=18)
            pl1["font"] = ft
            pl1["fg"] = "#000000"
            pl1["bg"] = "#ebd3f7"
            pl1["justify"] = "center"
            pl1["text"] = "0"
            pl1.place(x=40, y=80, width=70, height=25)

            ft = tkFont.Font(family='Times', size=10)
            label2["font"] = ft
            label2["fg"] = "red"
            label2["bg"] = "#ebd3f7"
            label2["justify"] = "center"
            label2["text"] = "Player 2:"
            label2.place(x=330, y=50, width=70, height=25)

            ft = tkFont.Font(family='Times', size=18)
            pl2["font"] = ft
            pl2["fg"] = "red"
            pl2["bg"] = "#ebd3f7"
            pl2["justify"] = "center"
            pl2["text"] = "0"
            pl2.place(x=310, y=80, width=70, height=25)

            label0 = tk.Label(root)
            ft = tkFont.Font(family='Times', size=23)
            label0["font"] = ft
            label0["bg"] = "#ebd3f7"
            label0["fg"] = "#000000"
            label0["justify"] = "center"
            label0["text"] = "Memory tiles"
            label0.place(x=100, y=30, width=215, height=52)

            btn[0].place(x=50, y=120, width=55, height=55)
            btn[1].place(x=120, y=120, width=55, height=55)
            btn[2].place(x=190, y=120, width=55, height=55)
            btn[3].place(x=260, y=120, width=55, height=55)
            btn[4].place(x=330, y=120, width=55, height=55)
            btn[5].place(x=50, y=190, width=55, height=55)
            btn[6].place(x=120, y=190, width=55, height=55)
            btn[7].place(x=190, y=190, width=55, height=55)
            btn[8].place(x=50, y=260, width=55, height=55)
            btn[8].place(x=190, y=260, width=55, height=55)
            btn[8].place(x=260, y=190, width=55, height=55)
            btn[9].place(x=330, y=190, width=55, height=55)
            btn[10].place(x=50, y=260, width=55, height=55)
            btn[11].place(x=120, y=260, width=55, height=55)
            btn[12].place(x=190, y=260, width=55, height=55)
            btn[13].place(x=260, y=260, width=55, height=55)
            btn[14].place(x=330, y=260, width=55, height=55)
            btn[15].place(x=50, y=330, width=55, height=55)
            btn[16].place(x=120, y=330, width=55, height=55)
            btn[17].place(x=190, y=330, width=55, height=55)
            btn[18].place(x=260, y=330, width=55, height=55)
            btn[19].place(x=330, y=330, width=55, height=55)

        def call():
            global j, btn, images, cnt2, cnt1, square, pair
            global clientAddress, serverPort, serverSocket

            def timer2(a, b):
                time.sleep(1)
                a.config(image=square)
                b.config(image=square)
                j[3] = 1

            message, clientAddress = serverSocket.recvfrom(2048)
            if (message == b'0'):
                return
            k1 = int.from_bytes(message, 'big')
            btn[k1].config(image=images[k1])
            time.sleep(1)
            message, clientAddress = serverSocket.recvfrom(2048)
            k2 = int.from_bytes(message, 'big')
            btn[k2].config(image=images[k2])
            if (images[k2] == images[k1]):
                cnt2 += 1
                pl2.config(text=str(cnt2))
                pair -= 1
                btn[k1].config(state="disabled")
                btn[k2].config(state="disabled")
                j[3] = 1
            else:
                thread2 = Thread(target=timer2, args=(btn[k1], btn[k2]))
                thread2.start()

            pl2.config(fg="black")
            pl1.config(fg="red")
            label1.config(fg="red")
            label2.config(fg="black")

        pl1 = tk.Label(root)
        pl2 = tk.Label(root)
        label1 = tk.Label(root)
        label2 = tk.Label(root)
        place()
        if (player == 1):
            root.title("MemoryTiles - Player1")
            thread = Thread(target=call)
            thread.start()
        else:
            root.title("MemoryTiles - Player2")

    def server(self, i):
        global j, btn, images, cnt2, cnt1, square, pair
        global clientAddress, serverPort, serverSocket

        def call():
            global j, btn, images, cnt2, cnt1, square, pair
            global clientAddress, serverPort, serverSocket

            pl1.config(fg="black")  # server
            pl2.config(fg="red")
            label2.config(fg="red")
            label1.config(fg="black")

            def timer2(a, b):
                time.sleep(1)
                a.config(image=square)
                b.config(image=square)
                pl2.config(fg="black")
                pl1.config(fg="red")
                label1.config(fg="red")
                label2.config(fg="black")
                j[3] = 1

            message, serverAddress = serverSocket.recvfrom(2048)
            if (message == b'0'):
                return
            k1 = int.from_bytes(message, "big")
            btn[k1].config(image=images[k1])
            time.sleep(1)
            message, serverAddress = serverSocket.recvfrom(2048)
            k2 = int.from_bytes(message, "big")
            btn[k2].config(image=images[k2])

            if (images[k2] == images[k1] and btn[k2] != btn[k1]):
                cnt2 += 1
                pl2.config(text=str(cnt2))
                pair -= 1
                btn[k1].config(state="disabled")
                btn[k2].config(state="disabled")
                if (pair == 0):
                    self.game_Over()
                    return
                pl2.config(fg="black")
                pl1.config(fg="red")
                label1.config(fg="red")
                label2.config(fg="black")
                j[3] = 1
            else:
                t3 = Thread(target=timer2, args=(btn[k1], btn[k2]))
                t3.start()

        t2 = Thread(target=call)

        def timer():
            global j
            time.sleep(1)
            j[1].config(image=square)
            j[12].config(image=square)
            j[0] = 0
            j[1] = None
            j[12] = None
            j[2] = None
            t2.start()

        if (j[3] == 1):  # red je na plejera 1
            t = threading.Thread(target=timer)
            btn[i].config(image=images[i])
            if (j[0] == 0):
                serverSocket.sendto(i.to_bytes(5, 'big'), clientAddress)
                j[2] = images[i]
                j[1] = btn[i]
                j[0] += 1
                return
            else:
                j[12] = btn[i]
                serverSocket.sendto(i.to_bytes(5, 'big'), clientAddress)
                if (j[2] == images[i] and j[1] != j[12]):
                    cnt1 += 1
                    pl1.config(text=str(cnt1))
                    pair -= 1
                    j[1].config(state="disabled")
                    j[12].config(state="disabled")
                    if (pair == 0):
                        self.game_Over()
                        return
                    j[0] = 0
                    j[1] = None
                    j[12] = None
                    j[2] = None
                    j[3] = 2
                    t2.start()  # call
                else:
                    j[3] = 2
                    t.start()

    def client(self, i):
        global j, btn, images, cnt2, cnt1, square, pair
        global serverName, serverPort, clientSocket

        def timer2(a, b):
            time.sleep(1)
            a.config(image=square)
            b.config(image=square)
            pl1.config(fg="black")
            pl2.config(fg="red")
            label2.config(fg="red")
            label1.config(fg="black")
            j[3] = 2

        def call2():
            global j, btn, cnt2, cnt1, pair

            pl2.config(fg="black")
            pl1.config(fg="red")
            label1.config(fg="red")
            label2.config(fg="black")
            response, serverAddress = clientSocket.recvfrom(2048)
            if (response == b'0'):
                return
            k1 = int.from_bytes(response, 'big')
            btn[k1].config(image=images[k1])
            time.sleep(1)
            response, serverAddress = clientSocket.recvfrom(2048)
            k2 = int.from_bytes(response, 'big')
            btn[k2].config(image=images[k2])
            if (images[k2] == images[k1] and btn[k2] != btn[k1]):
                cnt1 += 1
                pl1.config(text=str(cnt1))
                pair -= 1
                btn[k1].config(state="disabled")
                btn[k2].config(state="disabled")
                if (pair == 0):
                    self.game_Over()
                    return
                pl1.config(fg="black")
                pl2.config(fg="red")
                label2.config(fg="red")
                label1.config(fg="black")
                j[3] = 2
            else:
                t3 = Thread(target=timer2, args=(btn[k1], btn[k2]))
                t3.start()

        t2 = Thread(target=call2)

        def timer():
            global j
            time.sleep(1)
            pl2.config(fg="black")
            pl1.config(fg="red")
            label1.config(fg="red")
            label2.config(fg="black")
            j[1].config(image=square)
            j[12].config(image=square)
            j[0] = 0
            j[1] = None
            j[12] = None
            j[2] = None
            t2.start()

        if (j[3] == 2):  # red je na plejera 2.
            btn[i].config(image=images[i])
            t = threading.Thread(target=timer)
            if (j[0] == 0):
                j[2] = images[i]
                j[1] = btn[i]
                j[0] += 1
                clientSocket.sendto(i.to_bytes(5, 'big'), (serverName, serverPort))
                return
            else:
                j[12] = btn[i]
                clientSocket.sendto(i.to_bytes(5, 'big'), (serverName, serverPort))
                if (j[2] == images[i] and j[1] != j[12]):
                    cnt2 += 1
                    pl2.config(text=str(cnt2))
                    pair -= 1
                    j[1].config(state="disabled")
                    j[12].config(state="disabled")
                    if (pair == 0):
                        self.game_Over()
                        return
                    j[0] = 0
                    j[1] = None
                    j[12] = None
                    j[2] = None
                    j[3] = 1
                    t2.start()
                else:

                    j[3] = 1
                    t.start()

    def game_Over(self):
        global cnt1, cnt2
        if (cnt1 > cnt2):
            messagebox.showinfo("MemoryTiles", "Game Over - Player 1 wins!")
        elif (cnt2 > cnt1):
            messagebox.showinfo("MemoryTiles", "Game Over - Player 2 wins!")
        else:
            messagebox.showinfo("MemoryTiles", "Game Over - Tie")
        serverSocket.close()
        clientSocket.close()
        r.destroy()

    def close_root(self):
        if (j[3] == 1 and pl == 2):
            serverSocket2 = socket(AF_INET, SOCK_DGRAM)
            serverSocket2.bind(('', 1500))
            serverSocket2.sendto(b'0', (ip_got, 1500))
            serverSocket2.close()
        elif ((j[3] == 2 and pl == 1) or (j[3] == 0 and pl == 1)):
            clientSocket2 = socket(AF_INET, SOCK_DGRAM)
            clientSocket2.sendto(b'0', (serverName, serverPort))
            clientSocket2.close()
        serverSocket.close()
        clientSocket.close()
        r.destroy()


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()

exit(0)