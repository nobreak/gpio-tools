# connect pin 1 (+) with resistor
# than the resistor with long ledge of LED
# than short lege of LED with PIN 11 (-) GPIO 17



import time
import RPi.GPIO as GPIO

timeToSleep = 0.125

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) als Output
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(11, GPIO.HIGH)
GPIO.output(12, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)

# Dauersschleife fr das Blinken
while 1:
  GPIO.output(11, GPIO.LOW)
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(15, GPIO.HIGH)
  GPIO.output(16, GPIO.HIGH)
  time.sleep(timeToSleep)
  
  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.LOW)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(15, GPIO.HIGH)
  GPIO.output(16, GPIO.HIGH) 
  time.sleep(timeToSleep)

  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.LOW)
  GPIO.output(15, GPIO.HIGH)
  GPIO.output(16, GPIO.HIGH) 
  time.sleep(timeToSleep)

  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(15, GPIO.LOW)
  GPIO.output(16, GPIO.HIGH)
  time.sleep(timeToSleep)

  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(15, GPIO.HIGH)
  GPIO.output(16, GPIO.LOW)
  time.sleep(timeToSleep)

  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(15, GPIO.LOW)
  GPIO.output(16, GPIO.HIGH)
  time.sleep(timeToSleep)

  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.HIGH)
  GPIO.output(13, GPIO.LOW)
  GPIO.output(15, GPIO.HIGH)
  GPIO.output(16, GPIO.HIGH)
  time.sleep(timeToSleep)

  GPIO.output(11, GPIO.HIGH)
  GPIO.output(12, GPIO.LOW)
  GPIO.output(13, GPIO.HIGH)
  GPIO.output(15, GPIO.HIGH)
  GPIO.output(16, GPIO.HIGH)
  time.sleep(timeToSleep)
