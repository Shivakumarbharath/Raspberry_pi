import RPi.GPIO as gpio #to use the gpio pins in pi
from time import sleep

#We need to Initialise the board or bcm pin numbering schemes
gpio.setmode(gpio.BOARD)
pin=40
#Tell whether the pin is input or output
gpio.setup(pin,gpio.OUT)

#switch on the led
gpio.output(pin,True)
print("LED Light ON")
sleep(5)


gpio.output(pin,False)
print("\n\nLED Light OFF")
#Cleanup the gpio pins 
#Ensures not to get any error messages while using it again
gpio.cleanup()
