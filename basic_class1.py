import pywhatkit as pwk 
import time, webbrowser, os

from pywhatkit import history
def restart() :
    values = input("enter your message please add quotes before and after: ")
    value1 = input("enter country code to send message to:")
    value2 = input("enter the phone number excluding country code to send message to:")
    value3 = input("enter hour to send message in format(hh): ")
    value4 = input("enter min to send message in format(mm): ") 
    pwk.sendwhatmsg(f'"'+value1+"{"+value2+'}"',values,value3,value4)
    time.sleep(5)
    #os.system("taskkill /im webbrowser /f")
    restart()
restart()
