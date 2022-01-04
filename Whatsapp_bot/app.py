#https://circuitdigest.com/microcontroller-projects/whatsapp-automation-using-python-on-raspberry-pi-a-personalized-whatsapp-bot-for-home-automation
import pyautogui as pygu #To move mouse cursor and make click and keyboard strokes
from time import sleep #for delay
import pyperclip #to copy and past data
#import webbrowser #to open webbrowser
import os #to close webbrowser
import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time                              # calling for time to provide delays in program
pin1=40
IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
IO.setup(pin1,IO.OUT)             # initialize digital pin40 as an output.


def End():
    IO.output(pin1,False)
    IO.cleanup()
    exit()

#Open the default webbrowser and open web.whastapp
#webbrowser.get('chromium-browser').open('https://web.whatsapp.com/')
#print("Whatsapp Opened")
x=90
y=50
default_message = [
    "Hi I am your Whatsapp Bot :robot \n from RaspberryPi. I can help you with basic home automation. You can try any of the following :notes \n commands",
    "*turn on light* - _Turns on the led connected to pi_",
    "*turn off light* - _Turns off the led connected to pi_"]

turn_on_light = [
    "Sure, your :bulb \n Light is now turned on"
]

turn_off_light = [
    "Okay, Your LED is not turned off"
]

#Wait for whatsapp page to
def open_whatsapp():
    # check if whatsapp opened successfully
    find_whatsapp_header = None
    while find_whatsapp_header is None:
        find_whatsapp_header = pygu.locateOnScreen("Whatsapp_header.png",grayscale=True, confidence=.8)
        print(find_whatsapp_header)
        if find_whatsapp_header is None:
        	pygu.screenshot('ss.png')
        	print("Problem")
        use_here_button_pos = pygu.locateOnScreen("use_here_button.JPG", confidence=.8)
        if (use_here_button_pos):
            print("Whatsapp is being used somewhere else, clicking on use here")
            sleep(2)
            pygu.moveTo(use_here_button_pos[0], use_here_button_pos[1], duration=0.5)
            pygu.click()
        print(".")
        sleep(2)
    return 1

#checks for new message and opens it
def new_chat_available():
    # Check for new messages
    green_circle_pos = pygu.locateOnScreen("green_circle.JPG", confidence=.8)
    
    if (green_circle_pos):
        pygu.moveTo(green_circle_pos[0], green_circle_pos[1], duration=0.5)
        pygu.click()
        ok_button_pos = pygu.locateOnScreen("ok_button.JPG", confidence=.8)
        if (ok_button_pos):
            pygu.moveTo(ok_button_pos[0], ok_button_pos[1], duration=0.5)
            pygu.click()

        return 1
    else:
        return 0

def read_last_message():
    smily_paperclip_pos = pygu.locateOnScreen("smily.png", confidence=.8)
    pygu.moveTo(smily_paperclip_pos[0], smily_paperclip_pos[1])
    pygu.moveTo(smily_paperclip_pos[0] + x, smily_paperclip_pos[1] - y, duration=0.5)
    pygu.tripleClick()
    pygu.hotkey('ctrl', 'c')
    k=pyperclip.paste()
    return k

def get_response(incoming_message):
    if "CD_BOT" in incoming_message:
        return default_message
    elif "End" in incoming_message:
        End()
    if "turn on light" in incoming_message:
        IO.output(pin1,True)                      # turn the LED on
        return turn_on_light
    if "turn off light" in incoming_message:
        IO.output(pin1,False)                      # turn the LED off
        return turn_off_light
    else:
        return ""



def send_message(content):
    for content in message_content:
        pygu.typewrite(content)
        pygu.hotkey('shift', 'enter')
    sleep(1)
    send = pygu.locateOnScreen("send.png", confidence=.8)
    send=pygu.center(send)
    pygu.moveTo(send[0],send[1])
    pygu.click()
#    pygu.press('enter') #Enter key to send the message

def new_message_available():
    current_mouse_pos = pygu.position()
    pointer_color = pygu.pixel(current_mouse_pos[0], current_mouse_pos[1])
    if (pointer_color == (255, 255, 255)):
        return 1
    else:
        return 0

try:
    if (open_whatsapp()): #if whatsapp page is opened successfully
        print("##Whatsapp page ready for automation##")

    while(1):

        if (new_chat_available() or new_message_available()):
            print("New chat or message is available")
            incoming_message = read_last_message() #read the last message that we received
            print(incoming_message)
       
            message_content = get_response(incoming_message) #decide what to respond to that message
            print(message_content)
            if message_content != "":
                send_message(message_content) #send the message to person

            dummy = pygu.locateOnScreen("dummy.png", confidence=.8)
            dummy=pygu.center(dummy)
            pygu.moveTo(dummy[0],dummy[1])
            pygu.click()
except Exception as e :
    print(e)
    End()
