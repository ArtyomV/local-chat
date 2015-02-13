import socket
from threading import Thread

def connect(conn,connects):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        for el in connects:
            el.send(data.upper())
sock = socket.socket()
sock.bind(('', 7313))
sock.listen(1)
connects = []
while True:
    conn, addr = sock.accept()

    connects.append(conn)
    th1=Thread(target=connect,args=(conn,connects,))
    print("Connected", addr)
    th1.start()
    print(connects)
