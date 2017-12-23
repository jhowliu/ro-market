import os
import time
import pyautogui

from app.scripts.utils import find_coordinates

class AutoController(object):

    def __init__(self):
        pass

    @staticmethod
    def click(coords):
        """
        find location matched the given coordinates and click.

        @params:
            x, y: coordinates

        @return:
            True/False (isSuccess)
        """
        if coords is None: return False

        pyautogui.click(coords)
        time.sleep(0.5)

        return True

    @staticmethod
    def scroll(x, y, down=True):
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
