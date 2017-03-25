# connect pin 1 (+) with resistor
# than the resistor with long ledge of LED
# than short lege of LED with PIN 11 (-) GPIO 17



import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 7  als Output
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,1) # setze die Pulslaenge auf 1Hz (1x pro Sekunde)  

p.start(0) # starte mit 0% der Zeit ist die LED aus
p.ChangeDutyCycle(50)
try:
  while 1:
    for frequence in range(1,41,1): # schalte aller 0.01 sec die LED um 1 Prozent laenger aus, wir beginnen bei 15 um nicht komplett off zu sein
      p.ChangeFrequency(frequence)
      time.sleep(0.5)
    for frequence in range(40, 1, -1): # schalte aller 0.01 sec die LED um 1 Prozent kuerzer aus, bis maximal 15 % um nicht komplett off zu sein
      p.ChangeFrequency(frequence)
      time.sleep(0.5) 
except KeyboardInterrupt:
  pass
p.stop()

GPIO.cleanup()
