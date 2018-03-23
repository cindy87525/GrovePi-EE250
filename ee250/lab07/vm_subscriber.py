"""EE 250L Lab 07 Skeleton Code

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):

    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("anrg-pi14/ultrasonicRanger")
    client.subscribe("anrg-pi14/button")
    client.message_callback_add("anrg-pi14/led", led_callback)
    client.message_callback_add("anrg-pi14/button", button_callback)


#Default message callback. Please use custom callbacks.

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))

def ultrasonicRanger_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload, "utf-8")))

def button_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload, "utf-8")))


if __name__ == '__main__':
#this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:

        time.sleep(1)
        
            

