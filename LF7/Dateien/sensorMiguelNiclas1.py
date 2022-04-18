# Benoetigte Module werden importiert und eingerichtet
import RPi.GPIO as GPIO
import time

# GPIO Modus wird gesetzt, Warnungen ausgeschaltet
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Hier wird der Eingangs-Pin deklariert, an dem der Sensor angeschlossen ist.
# Zusaetzlich wird auch der Signal-Pin für den Output (LED) deklariert
GPIO_PIN = 24
GPIO_SIGNAL = 12

# GPIO Setup für Input / Lichtschranke
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
print ("Sensor-Test [druecken Sie STRG+C, um den Test zu beenden]")

# GPIO Setup für Output LED Signal
GPIO.setup(GPIO_SIGNAL, GPIO.OUT, initial=GPIO.HIGH)

# Diese AusgabeFunktion wird bei Signaldetektion ausgefuehrt und lässt das LED ausgehen
def ausgabeFunktion(null):
    print("Signal erkannt")
    GPIO.output(GPIO_SIGNAL, GPIO.LOW)
    
# Beim Detektieren eines Signals (steigende Signalflanke) wird die Ausgabefunktion ausgeloest
GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=ausgabeFunktion, bouncetime=100)

# Hauptprogrammschleife
try:
    while True:
        time.sleep(1)
        
# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:
    GPIO.cleanup()
