"""EE 250L Lab 07 Skeleton Code

Run vm_publisher.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from pynput import keyboard

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("anrg-pi14/led")
    client.subscribe("anrg-pi14/lcd")
#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))
    print("on_message: msg.payload is of type " + str(type(msg.payload)))

def led_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload, "utf-8")))

def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    
    if k == 'w':
        print("w")
        #send "w" character to rpi
        client.publish("anrg-pi14/lcd", "w")
    elif k == 'a':
        print("a")
        # send "a" character to rpi
         #send "LED_ON"
        client.publish("anrg-pi14/led", "LED_ON!")
        client.publish("anrg-pi14/lcd", "a")
    elif k == 's':
        print("s")
        # send "s" character to rpi
        client.publish("anrg-pi14/lcd", "s")
    elif k == 'd':
        print("d")
        # send "d" character to rpi
        # send "LED_OFF"
        client.publish("anrg-pi14/led", "LED_OFF!")
        client.publish("anrg-pi14/lcd", "d")

if __name__ == '__main__':
    #setup the keyboard event listener
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread

    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()


    while True:
        
        time.sleep(1)
            
            

