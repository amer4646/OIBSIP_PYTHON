#server.py      ##execute server.py first

#IMPORTING LIBRARIES
import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()                   #getting host name using socket
print("server will start on host:",host)
port=8080                           #port number(change it according to your requirement)
s.bind((host,port))
print("")
print("Server done binding to host and port sccessfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn,addr=s.accept()
print(addr,"Has connected to server")   
print("")
while 1:
    message=input(str(">>"))
    message=message.encode()
    conn.send(message)
    print("Message sent")
    print("")
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print("Client:",incoming_message)
    print("")
