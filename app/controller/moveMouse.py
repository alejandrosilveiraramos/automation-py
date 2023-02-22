import pyautogui as p


def mouseLocation():
    # create a new instance using sleep from pyautogui
    p.sleep(5)
    
    # mouse position
    position = currentMouseX, currentMouseY = p.position()
    
    return position

def mouseMovement():
    
    #create a new instance using moveTo from pyautogui
    p.moveTo(1870,211)

    
