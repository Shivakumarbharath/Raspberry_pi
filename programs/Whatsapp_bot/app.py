#https://circuitdigest.com/microcontroller-projects/whatsapp-automation-using-python-on-raspberry-pi-a-personalized-whatsapp-bot-for-home-automation
import pyautogui as pygu #To move mouse cursor and make click and keyboard strokes
from time import sleep #for delay
import pyperclip #to copy and past data
import os #to close webbrowser
import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time                              # calling for time to provide delays in program
pin1=40
pin2=37
pin3=35
pin4=33
pin5=38
pin6=36
pin7=32
pin8=31
pin9=29
pin10=22
#gnd=39

pins=[pin1,pin2,pin3,pin4,pin5,pin6,pin7,pin8,pin9,pin10]

status=[False,False,False,False,False,False,False,False,False,False]

IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
for e in pins:
#    print(e)
    IO.setup(e,IO.OUT)             # initialize digital pin40 as an output.




def End():

    for e in pins:
        IO.output(e,False)
    
    IO.cleanup()
    exit()

def mov_away():
    dummy = pygu.locateOnScreen("dummy.png", confidence=.8)
    dummy=pygu.center(dummy)
    pygu.moveTo(dummy[0],dummy[1])
    pygu.click()


#Open the default webbrowser and open web.whastapp
#webbrowser.get('chromium-browser').open('https://web.whatsapp.com/')
#print("Whatsapp Opened")
x=90
y=50
default_message = [
    "Hi I am your Bot :robot \n at your service.",
    " You can use any of the following :notes \n commands",
    "0. *Switch ON  all lights*",
    "00. *Switch OFF all the Lights ",
    "1. *Switch to light 1* - _Switch ON/OFF the led 1_",
    "2. *Switch to light 2* - _Switch ON/OFF the led 2_",
    "3. *Switch to light 3* - _Switch ON/OFF the led 3_",
    "","",
    "Type the number and send to control the lights",
    "",
    "Type *Status* to Check the Status of Each Light",
    "",
    "*NOTE* - Message me *Only* after I Reply",]

#if off and now on
turn_on_light = lambda x: [f"The Light {x} was OFF",f"The Light {x} is now switched *ON* :bulb \n "]

#if on and now off
turn_off_light = lambda x:[f"The Light {x} was ON :bulb \n",f"The Light {x} is now switched *OFF* "]

#End Message
end_message=["Your Bot is Signing OFF","You Cannot use the Service untill the Server is Run again Manually",'\n','\n',"Thank You"]

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
    #pygu.moveTo(smily_paperclip_pos[0], smily_paperclip_pos[1])
    pygu.moveTo(smily_paperclip_pos[0] + x, smily_paperclip_pos[1] - y, duration=0.5)
    pygu.tripleClick()
    pygu.hotkey('ctrl', 'c')
    k=pyperclip.paste()
    return k

def switch(num,pin):
    global status
    n=int(num)
    status[n-1]= not status[n-1]
    IO.output(pin,status[n-1])
    if status[n-1]:
        return turn_on_light(n)
    else:
        return turn_off_light(n)

def get_response(incoming_message):
    if "activate" in incoming_message:
        return default_message
    if "end" in incoming_message:
        send_message(end_message)
        End()
    if "status" in incoming_message:
        st=''
        dt={True:'ON',False:'OFF'}
        for i,e in enumerate(status):
            st+=f'Light {i+1} is {dt[e]} \n'
        return st.split('\n')
    if "0"== incoming_message:
        for i,e in enumerate(pins):
            IO.output(e,True)
            status[i]=True
        return ["All the Lights are ON"]
    if "00" ==incoming_message:
        for i,e in enumerate(pins):
            IO.output(e,False)
            status[i]=False
        return ["All the Lights are OFF"]
    if "1" in incoming_message:
        return switch("1",pin1)                      # turn the LED on

    if "2" in incoming_message:
        return switch("2",pin2)
    
    if "3" in incoming_message:
        return switch("3",pin3)

    if "4" in incoming_message:
        return switch("4",pin4)

    if "5" in incoming_message:
        return switch("5",pin5)

    if "6" in incoming_message:
        return switch("6",pin6)

    if "7" in incoming_message:
        return switch("7",pin7)

    if "8" in incoming_message:
        return switch("8",pin8)

    if "9" in incoming_message:
        return switch("9",pin9)

    if "10" in incoming_message:
        return switch("10",pin10)



    else:
        return ""



def send_message(message_content):
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
 #       send_message(["The Server has been Started","",""]+default_message)
    while(1):

        if (new_chat_available()): # or new_message_available()):
            print("New chat or message is available")
            incoming_message = read_last_message() #read the last message that we received
            print("Message Recieved -",incoming_message)
       
            message_content = get_response(incoming_message.lower()) #decide what to respond to that message
            print("Response That will be sent--- \n",'\n'.join(message_content))
            if message_content != "":
                send_message(message_content) #send the message to person
            mov_away()
            
except Exception as e :
    print(e)
    End()
