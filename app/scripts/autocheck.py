import os
import pytesseract
import pyautogui

from PIL import Image

from app import config

from app.scripts.utils import keep_numerics
from app.scripts.utils import FindCoordinates

class AutoCheck(object):

    def __init__(self):

        self._zeny_icon = Image.open(config.ZENY_ICON)

    def get_all_price(self):
        """
        Get the all prices on the screen

        @return
            prices: [int]
        """
        # in order to skip the zeny icon

        results = []
        skip_width = int(self._zeny_icon.width/2)

        # middle points
        targets = FindCoordinates.locate_all_targets(self._zeny_icon)

        for x, y in targets:
            correction_coords = (x+skip_width, y+_zeny_icon.height/2)
            img = self._capture_target(correction_coords[0], correction_coords[1], 100, self._zeny_icon.height)
            img.show()
            #price = self._recognize_price(img)
            #results.append(price)

        return results

    def _capture_target(self, x, y, window_width, window_height):
        """
        Take a shot on x, y
        """
        return pyautogui.screenshot(region=(x, y, window_width, window_height))


    def _recognize_price(self, img):
        """
        use tesseract OCR to recognize digits

        @params
            img: given Image

        @return
            number: Int
        """
        # use the ro.traineddata
        tesseract_config = "-l ro"

        predict = pytesseract.image_to_string(img, config=tesseract_config)

        return keep_numerics(predict)
