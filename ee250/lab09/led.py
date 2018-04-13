import time
import grovepi

# Connect the Grove LED to digital port D5
# SIG,NC,VCC,GND
led = 3

# Digital ports that support Pulse Width Modulation (PWM)
# D3, D5, D6

# Digital ports that do not support PWM
# D2, D4, D7, D8

grovepi.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0

while True:


    grovepi.digitalWrite(led,1)
    time.sleep(.5)
    grovepi.digitalWrite(led,0)
    time.sleep(.5)
