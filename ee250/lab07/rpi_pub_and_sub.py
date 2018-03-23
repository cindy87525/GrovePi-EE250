"""EE 250L Lab 07 Skeleton Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""
import sys
sys.path.append('../../Software/Python/')
import paho.mqtt.client as mqtt
import time
import grovepi


button = 2
led = 3
ultrasonic_ranger = 4
grovepi.pinMode(led,"OUTPUT")
grovepi.pinMode(button,"INPUT")




def led_callback(client, userdata, message):
    global led
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))

    data = str(message.payload, "utf-8")

    if data == "LED_ON!":
        grovepi.digitalWrite(led,1)     # Send HIGH to switch on LED
        print ("LED_ON!")
        time.sleep(1)
    if data == "LED_OFF!":
        grovepi.digitalWrite(led,0)     # Send LOW to switch off LED
        print ("LED_OFF!")
        time.sleep(1)

def button_callback(client, userdata, message):
    global button
    print("custom_callback: " + message.topic + " " + str(message.payload, "utf-8"))
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))

    data = str(message.payload, "utf-8")


    print ("Button_pressed!")
    client.publish("anrg-pi14/button", "Button_pressed!")
    time.sleep(1)



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("anrg-pi14/led")
    client.subscribe("anrg-pi14/ultrasonicRanger")
    client.subscribe("anrg-pi14/button")
    client.message_callback_add("anrg-pi14/led", led_callback)
    client.message_callback_add("anrg-pi14/button", button_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()


            



    while True:
        print(grovepi.ultrasonicRead(ultrasonic_ranger))
        time.sleep(1)
            

