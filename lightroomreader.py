import time, webbrowser, os
def restart() :
    values = input("enter 3-4 random characters: ")
    webbrowser.open("www.prnt.sc/nt"+ values )
    time.sleep(5)
    os.system("taskkill /im webbrowser /f")
    restart()
restart()             