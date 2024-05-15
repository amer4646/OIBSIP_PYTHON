#client.py      ##execute client.py after executing server.py

#importing libraries
import socket
import sys
import time

s=socket.socket()
host=input(str("Enter HostName of the server:"))    #enter hostname from server.py
port=8080                       #port number should be same in server.py and client.py
s.connect((host,port))
print("Connected to the server")
while 1:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    print("Server:",incoming_message)
    print("")
    message=input(str(">>"))
    message=message.encode()
    s.send(message)
    print("Message has been sent")
    print("")
