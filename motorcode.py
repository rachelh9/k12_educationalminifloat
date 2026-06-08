from machine import Pin, I2C, PWM
import ms5803
import time
from time import sleep
from time import sleep_ms
import urtc

p1=Pin(12,Pin.IN) # c2 pin on motor - yellow
p2=Pin(14,Pin.IN) # c1 pin on motor - green

i2c = I2C(scl=Pin(5), sda = Pin(4))
rtc = urtc.DS3231(i2c)

# ── pins ──────────────────────────────────────────────────────────────────────
IN1_PIN       = 13
IN2_PIN       = 15
ENA_PIN       = 2  # pwm pin
ENCODER_A_PIN = 14
ENCODER_B_PIN = 12
LED_PIN       = 0

# ── constants ─────────────────────────────────────────────────────────────────
GEARING     = 20
ENCODERMULT = 12
UP     = True
DOWN    = False

# ── hardware init ─────────────────────────────────────────────────────────────
in1 = Pin(IN1_PIN, Pin.OUT)
in2 = Pin(IN2_PIN, Pin.OUT)
ena = PWM(Pin(ENA_PIN), freq=1000) # 1kHz PWM frequency

enc_a = Pin(ENCODER_A_PIN, Pin.IN, Pin.PULL_UP)
enc_b = Pin(ENCODER_B_PIN, Pin.IN, Pin.PULL_UP)
led = Pin(LED_PIN, Pin.OUT)
#led.on()

# ── motor control ─────────────────────────────────────────────────────────────
def motor_run(direction: bool):
    if direction == UP:
        in1.on()
        in2.off()
    else:
        in1.off()
        in2.on()

def motor_stop():
    in1.off()
    in2.off()
    ena.duty(0)

#cannot set motor speed unless there's a change in voltage input
#def motor_set_speed(speed: int): 
#    duty = min(speed, 255) * 4
#    ena.duty(duty)

    

