import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
def dec2bin(a):
    a = [int(i) for i in bin(a)[2:]]
    while len(a) != 8:
        a = [0]+a
    return a
try:
    period =float(input("Введите период треугольного сигнала(секунды):"))
    step_time = period / 510
    # 255 вверх и 255 вниз

    while True:
        for a in range(256):
            GPIO.output(dac,dec2bin(a))
            time.sleep(step_time)

        for a in range(254, 0, -1):
            GPIO.output(dac,dec2bin(a))
            time.sleep(step_time)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup(dac)