#DutyCycle = PulseWidth*frequency=.001 *50 = .05 = 5%

'''
So, for a 50 Hz signal, if we set the DutyCycle to 5, then we should see 
the servo move to the full left position. Similarly, if we set DutyCycle to 7.5, 
we should get the middle position, and if we set it to 
10 we should be in the full right position. You can get all the 
intermediate positions by linearly scaling between 5 and 10. Note that 
these values will vary between brands, and between individual servos, so 
play around with your servo to get it calibrated. We are now ready 
to apply a command to position the servo. If we want the servo in the 
full left position, we should set the DutyCycle to 5%. '''
import time
import RPi.GPIO as gpio

#initialise board
gpio.setmode(gpio.BOARD)

#set 11 as output
gpio.setup(11,gpio.OUT)

pwm=gpio.PWM(11,50)

pwm.start(5)
time.sleep(3)
pwm.ChangeDutyCycle(7.5)
time.sleep(3)
pwm.ChangeDutyCycle(10)
time.sleep(3)
#pwm.ChangeDutyCycle(5)

# now we can change it to desired angle
DutyCycle =lambda DesiredAngle:1/20* (DesiredAngle) + 2
inp=None
while(inp!='q'):
	if inp:=input("Enter the Angle ?")=='q':
		break;
	inp=int(inp)
	pwm.ChangeDutyCycle(DutyCycle(inp))
	pwm.ChangeFrequency(50)
gpio.cleanup()
