# connect pin 1 (+) with resistor
# than the resistor with long ledge of LED
# than short lege of LED with PIN 11 (-) GPIO 17



import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 7  als Output
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,1) # setze die Pulslaenge auf 1Hz (eine Sekunde)  

p.start(0) # starte mit 0% der Zeit ist die LED aus

while 1:
  p.ChangeDutyCycle(75) # run loop - 75 % der Zeit ist die Lampe aus



#p.stop()

#GPIO.cleanup()
