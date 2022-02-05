import RPi.GPIO as gpio #to use the gpio pins in pi
from time import sleep

#We need to Initialise the board or bcm pin numbering schemes
gpio.setmode(gpio.BOARD)

#Tell whether the pin is input or output
gpio.setup(11,gpio.OUT)

#create a pwm object
my_pwm=gpio.PWM(11,100) #syntax-gpio.PWM(pin_no,Frequency)

#start pwm
my_pwm.start(50) # with 50% duty cycle
sleep(5)

#change dutycycle
print("Duty Cycle-100")
my_pwm.ChangeDutyCycle(100)

sleep(5)
print("Duty Cycle -25")
my_pwm.ChangeDutyCycle(25)

sleep(5)
print("Duty Cycle-50")
my_pwm.ChangeDutyCycle(50)


#change frequuency
print("Frequency change to 1000")
my_pwm.ChangeFrequency(1000)
sleep(5)


#Cleanup the gpio pins 
#Ensures not to get any error messages while using it again
gpio.cleanup()
