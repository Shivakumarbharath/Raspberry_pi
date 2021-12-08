import RPi.GPIO as gpio #to use the gpio pins in pi
from time import sleep

#We need to Initialise the board or bcm pin numbering schemes
gpio.setmode(gpio.BOARD)

#Tell whether the pin is input or output
gpio.setup(11,gpio.OUT)

#switch on the led
gpio.output(11,True)
print("LED Light ON")
sleep(5)


gpio.output(11,False)
print("\n\nLED Light OFF")
#Cleanup the gpio pins 
#Ensures not to get any error messages while using it again
gpio.cleanup()
