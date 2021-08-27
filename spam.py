import pyautogui,time
time.sleep(15)
def restart():
    pyautogui.click()
    #copy and paste last copy
    pyautogui.press('ctrl'+'v')
    #send
    pyautogui.press('enter')
    time.sleep(0.01)
    restart()
restart()
time.sleep(2.00)
quit()
