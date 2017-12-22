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
            True/False (isSuccess)
        """
        try:
            target = pyautogui.locateCenterOnScreen(img)
            pyautogui.click(target)
        except Exception as ex:
            print('Cannot locate the given image in the screen')
            return False

        return true

    def scroll(self, x, y, down=True):
        """
        scroll the screen on the given point(x, y)

        @params:
            x, y = the given screen point(x, y)
            down: chekc if you want to scroll down

        @return:
            True/False (isSuccess)
        """
        scroll_amount = 100 + (-200 * down)
        # negative is scroll-down
        try:
            pyautogui.scroll(scroll_amount, x, y)
        except Exception as ex:
            print('Cannot locate the given image in the screen')
            return False

        return True
