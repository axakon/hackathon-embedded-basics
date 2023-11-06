import machine # Contains all functions related to the Pi Pico hardware
from machine import Pin, ADC, PWM # Easier way of using pin, ADC and PWM
import utime # Handles waiting and time
import network # Handles connecting to WiFi
import urequests # Handles HTTP requests

# Define the pins
LED_PIN = 18 # Mode = OUT (Output)
BUTTON_PIN = 19 # Mode = IN (Input)
POTENTIOMETER_PIN = 26

# Setup the pins here (LED is on the house)
led = Pin(LED_PIN, mode=Pin.OUT)

# Setup the ADC here
# https://docs.micropython.org/en/latest/rp2/quickref.html#adc-analog-to-digital-conversion

# Setup the PWM here
# https://docs.micropython.org/en/latest/rp2/quickref.html#pwm-pulse-width-modulation

# Connect to WiFi here, before the main loop
# https://docs.micropython.org/en/latest/library/network.WLAN.html

# Print something that we are all setup and just started the main loop
print("Raspberry Pi Pico is now all booted and running!")

# The almighty infinite main while loop
while True:
    ...
