import pyautogui,time
time.sleep(15)
def restart():
    pyautogui.click()
    pyautogui.press('ctrl'+'v')
    pyautogui.press('enter')
    time.sleep(0.01)
    restart()
restart()
