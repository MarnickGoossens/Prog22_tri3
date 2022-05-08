import RPi.GPIO as GPIO  # Only works on Raspberry Pi
import time


class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)


led1 = Led(8)
led2 = Led(3)
led3 = Led(10)
led4 = Led(5)

while True:
    led1.on()
    led2.off()
    led3.on()
    led4.off()
    time.sleep(1)
    led1.off()
    led2.on()
    led3.off()
    led4.on()
    time.sleep(1)
