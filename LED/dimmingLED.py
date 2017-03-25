# connect pin 1 (+) with resistor
# than the resistor with long ledge of LED
# than short lege of LED with PIN 11 (-) GPIO 17



import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 7  als Output
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,60) # setze die Pulslaenge auf 60Hz (60x pro Sekunde) kein flackern mehr 

p.start(0) # starte mit 0% der Zeit ist die LED aus

try:
  while 1:
    for offTimeInPercent in range(15,101,1): # schalte aller 0.01 sec die LED um 1 Prozent laenger aus, wir beginnen bei 15 um nicht komplett off zu sein
      p.ChangeDutyCycle(offTimeInPercent)
      time.sleep(0.01)
    for offTimeInPercent in range(100, 14, -1): # schalte aller 0.01 sec die LED um 1 Prozent kuerzer aus, bis maximal 15 % um nicht komplett off zu sein
      p.ChangeDutyCycle(offTimeInPercent)
      time.sleep(0.01) 
except KeyboardInterrupt:
  pass
p.stop()

GPIO.cleanup()
