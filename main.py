from gpiozero import CPUTemperature, PWMLED
from time import sleep

pino = 26
temp_base = 50
temp_margin = 5
max_duty = 100
min_duty = 25

duty_cycle = min_duty

pwm = PWMLED(pino)
cpu = CPUTemperature()

try:
    while True:
        pwm.value = duty_cycle/100
        temp = cpu.temperature

        if temp > temp_base + temp_margin:
            duty_cycle += 20
        elif temp < temp_base - temp_margin:
            duty_cycle -= 10

        if duty_cycle < min_duty:
            duty_cycle = min_duty
        if duty_cycle > max_duty:
            duty_cycle = max_duty
        sleep(5)
except Exception as e:
    print(e)
