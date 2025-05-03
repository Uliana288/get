import RPi.GPIO as GPIO
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def binary(a):
    a = [int(i) for i in bin(a)[2:]]
    while len(a) != 8:
        a = [0]+a
    return a
try:
    while True:
        a = input("Введите число от 0 до 255 (или 'q' для выхода):")
        if a == "q":
            exit()
        elif num = float(a):
            if not num.is_integer():
                print("Это не целое число")
        elif int(a)<0:
            print("Это отрицательное число")
        else:
            try:
                a = int(a)
                if a > 255:
                    print("Число больше, чем 255")
                else:
                    GPIO.output(dac,binary(a))
                    print("Предполагаемое напряжение ЦАП:", a/255*3.3+0.03)

            except:
                print("Это не число")

finally:
    GPIO.output(dac,0)
    GPIO.cleanup(dac)