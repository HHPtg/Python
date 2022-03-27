import pyautogui,time
time.sleep(10)
def restart():
    pyautogui.click()
    #copy and paste last copy
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    #send
    pyautogui.press('enter')
    time.sleep(0.01)
    restart()
restart()
time.sleep(60.00)
quit()
