

import socket

def Main():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '127.0.0.1'
    port = 6003

    s = socket.socket()
    s.bind((host,port))


    while True:
        #data, addr = s.recvfrom(1024)
        #data = data.decode('utf-8')
        #print("Message From: " + str(addr))
        #print("From connected user: " + data)
        #data = data.upper()
        data = input("LED on or off?-> ")
        print("Sending: " + data)
        s.send(data.encode('utf-8'))
    c.close()







    # UDP is connectionless, so a client does not formally connect to a server
    # before sending a message.

    #message = input("message-> ")

if __name__ == '__main__':
    Main()



