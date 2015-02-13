import socket
from threading import Thread
from tkinter import *

def receive():
    while True:
        data = sock.recv(1024)
        tex.insert(1.0, data.decode()+'\n')

def send(event):
    text=nickname+': '+ent.get()
    sock.send(text.encode())
    ent.delete(0,END)
def set_nick(event):
    nick=nick_ent.get()
    return nick

sock = socket.socket()
sock.connect(('localhost', 7313))

th=Thread(target=receive, args=())
th.start()

root=Tk()
win = Toplevel(root,relief=SUNKEN,bg="blue")
win.title("Nickname")
win.minsize(width=300,height=50)
nick_ent=Entry(win, width=35)
nick_but=Button(win, text="Set Nickname")
nickname='nickname'
nick_but.bind("<Button-1>", set_nick)
print(nickname)
nick_ent.grid(row=0, column=0)
nick_but.grid(row=0, column=4, padx=10)
tex=Text(root, width=50, height=10, font=12, wrap=WORD)
scr = Scrollbar(root,command=tex.yview)
tex.configure(yscrollcommand=scr.set)
tex.grid(row=0,column=0, pady=23)
scr.grid(row=0,column=1, sticky=N+S)
ent = Entry(root,width=70)
ent.grid(row=6,column=0,)
but=Button(root, text="Send")
but.grid(row=6,column=6)
but.bind("<Button-1>", send)
ent.bind("<Return>", send)

mainloop()

sock.close()


