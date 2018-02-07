import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
os.fork()
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data or 'close' in data:
            break
        conn.send(data.encode())
    conn.close()
