import os
import pyautogui

class AutoController(object):

    def __init__(self):
        pass

    def click(self, img):
        """
        find location matched the given Image and click.

        @params:
            img: Image
        @return:
            success: true/false
        """
        try:
            target = pyautogui.locateCenterOnScreen(img)
            pyautogui.click(target)
        except Exception as ex:
            print('Cannot locate the given image in the screen')
            return False

        return true

    def scroll(self):
        pass
