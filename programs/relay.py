import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
pin=8
gpio.setup(pin,gpio.OUT)
status=True
try:
    while True:
        
        k=int(input("Choice ? :"))
        if k==1:
            status=not status
            gpio.output(pin,status)
            print("You Entered 1")
        else:
            print("Usage <1> Enter (1 is the switch)")

except KeyboardInterrupt as key:
    gpio.cleanup()
    print(key)

except Exception as e:
    print(e)
    gpio.cleanup()
