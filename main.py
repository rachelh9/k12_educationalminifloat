# automatically runs when microcontroller is given power

"""
Use Pin 16 to control sleep mode:
    When Pin 16 is connected to RST, Pin 16 is pulled high. This condition must be met for the sensor to sleep
    If Pin 16 is disconnected from RST and connected to a GND pin, the sensor does not go to sleep.
    > in our case: we can use a switch (connect p16 to middle, gnd & rst on either sides)
"""
from machine import Pin, I2C, PWM
from time import sleep
import floatprofile as fp
import motorcode as mc

mc.motor_stop()

print("waiting 10 seconds...")
sleep(10) #change this before deployment

#print("checking switch pin...")
#assign pin 16 for testing vs sampling mode
#p2=Pin(2,Pin.IN)
print("starting profiles")
fp.float_profile(3)

'''
if p2.value() == 0: #if pin16 connected to gnd --> in profiling mode (black switch)
    #float profile function here, set sample_time parameter
    print("starting profiles")
    fp.float_profile(3) #20 samples -- 30 seconds in total (15 up, 15 down)
        
else: # pin 16 is low (connected to ground) --> sleep (sampling mode) - red switch
    print("stopped in not profiling mode")
'''    




