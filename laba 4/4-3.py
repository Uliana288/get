import RPi.GPIO as GPIO
PWM_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(20, 1000)
pwm.start(0)

try:
    while True:
        duty = input("Введите коэффициент заполнения (0-100): ")
        try:
            duty_cycle = int(duty)
            if 0 <= duty_cycle <= 100:
                pwm.ChangeDutyCycle(duty_cycle)
                voltage = 3.3 * (duty_cycle / 100)
                print("Ожидаемое напряжение:", voltage)
            else:
                print("значение от 0 до 100")
        except ValutError:
            print("Введите целое число")

finally:
    pwm.stop()
    GPIO.cleanup()