# connect pin 1 (+) with resistor
# than the resistor with long ledge of LED
# than short lege of LED with PIN 11 (-) GPIO 17



import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) als Output
GPIO.setup(11, GPIO.OUT)

# Dauersschleife fr das Blinken
while 1:
  # LED aus
  GPIO.output(11, GPIO.LOW)
  print("LED ON")
  # eine Sekunde warten
  time.sleep(1.5)
  # LED an
  GPIO.output(11, GPIO.HIGH)
  print("LED OFF")  
# eine Sekunde warten
  time.sleep(1.5)
