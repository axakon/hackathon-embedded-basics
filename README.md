# Hackathon on Embedded Basics, November 8th
The first hackathon with a focus on embedded programming for Raspberry Pi Pico using Micropython

## Recommended setup
1. Download and install the [Thonny IDE](https://thonny.org/)
2. Clone this repo
3. Open the `main.py` file in Thonny
4. Connect the Raspberry Pi Pico to your computer using a USB cable, it should show up automatically after a couple of seconds. 
   If it doesn't show up, click on the current Python version in the bottom right corner and wait for a list to pop-up. 
   From this list, select "MicropPython (Raspberry Pi Pico)" (the name might also contain which physical port it is connected on). 
5. Press F5 or the green arrow button up in the top left part of the window to send your code to the Pi Pico and run it
6. You're off to the races, now complete the challenges below!

The boilerplate `main.py` file contains all imports and libraries (including links to the documentation) that you will need to complete the below challenges!

## Challenge
Your mission is to expand on the boilerplate code found in `main.py` by adding the following functions:
- Printing "Button pressed" (or similar) to the console when the button is pressed
- Turning the LED light on when the button is pressed and turning it of when the button is released
- Reading an analogue value from the potentiometer (the spinny thingy) using the ADC (Analogue to Digital Converter)
- Start dimming the LED light using PWM (Pulse Width Modultion) 
- Dim the LED using the value you read from the potentiometer
- Send a HTTP GET request using WiFi and the `urequests` library and display the incoming information in the console

## Bonus challenge
- Adding a toggle functionality to the button. Pressing it once should turn the LED on, and pressing it again should turn the LED off. 
    You will need to implement some basic input debounce, otherwise the LED will blink when pressing the button
- Send a HTTP POST request with data from the potentiometer, when the button is pressed
- Add a "press-and-hold" function to the button. Holding the button down should either dim or brighten the LED, until it is released 
