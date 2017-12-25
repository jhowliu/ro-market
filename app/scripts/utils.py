import re
import cv2
import pyautogui
import numpy as np
from PIL import Image


def keep_numerics(text):
    """
    keep the numerics from the given text

    @params
        text: text

    @return
        None/Int
    """
    result = None

    try:
        result = int(re.sub('[^0-9]', '', text))
    except Exception as ex:
        print("cannot get numerics")

    return None

class FindCoordinates(self):

    @staticmethod
    def locate_target(template_path, threshold=.9):
        """
        return the template img location

        @params
            template_path: path of template's file
            threshold: to limit template match accuracy (optional)

        @return
            middle: the middle point of the given template
        """

        template = cv2.imread(template_path)
        h, w = template.shape[:-1]

        img = pyautogui.screenshot().convert('L')
        img = np.array(img)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val < threshold: return None

        middle = (min_loc[0] + int(w/2), min_loc[1] + int(h/2))

        return middle

    @staticmethod
    def locate_all_targets(template_path, threshold=.9):
        targets = []

        template = cv.imread(template_path)
        h, w = template.shape[:-1]

        img = pyautogui.screenshot().convert('L')
        img = np.array(img)

        res = cv2.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            middle = (pt[0] + int(w/2), pt[1] + int(h/2))
            targets.append(middle)

        return targets
