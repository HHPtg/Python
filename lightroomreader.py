import time, subprocess
def restart() :
    values = input("enter any 4 random characters: ")
    p = subprocess.Popen(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "www.prnt.sc/nt"+values ])
    time.sleep(15)
    p.kill()
    restart()
restart()