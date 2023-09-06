#admin_server.py

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_pc = ""
port = 12345

s.bind((local_pc, port))
s.listen()

while True:
    print("Server Listening: ")
    conn, addr = s.accept()
    print("Connection OK: ", addr)

    try:
        while True:
            command = input("Command: ")
            conn.sendall(command.encode())
            
            
    except:
        print("Disconnected from : ", addr)
