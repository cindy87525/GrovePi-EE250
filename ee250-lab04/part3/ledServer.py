

import sys

# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')


import socket

import time
import grovepi
# Connect the Grove LED to digital port D3


def Main():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '192.168.1.209'
    port = 5001

    led = 3

    grovepi.pinMode(led,"OUTPUT")

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user: " + data)
        if data == "LED ON!"
            grovepi.digitalWrite(led,1)     # Send HIGH to switch on LED
            print ("LED ON!")
            time.sleep(1)
        if data == "LED OFF!"
            grovepi.digitalWrite(led,0)     # Send LOW to switch off LED
            print ("LED OFF!")
            time.sleep(1)
    c.close()







    # UDP is connectionless, so a client does not formally connect to a server
    # before sending a message.

    #message = input("message-> ")

if __name__ == '__main__':
    Main()



