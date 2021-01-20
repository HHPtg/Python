import json,webbrowser
def restart() :
    values = input("Enter 4 random characters : ") 
    base_url = "www.prnt.sc/nt"+values 
    response = webbrowser.open(base_url)
    restart()
restart()