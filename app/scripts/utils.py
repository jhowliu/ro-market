import os
import re
import cv2
import pyautogui
import numpy as np

from PIL import Image

from app import config

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

    return result

class FindCoordinates():

    @staticmethod
    def locate_target(template_path, threshold=.9):
        """
        return the template img location

        @params
            template_path: path of template's file
            threshold: to limit template match accuracy (optional)

        @return
            max_loc: the top_right point of the given template
        """
        template = cv2.imread(template_path)
        h, w = template.shape[:-1]

        # navie method
        tmp_file = os.path.join(config.__TMP__, 'tmp.png')
        pyautogui.screenshot(tmp_file)
        img = cv2.imread(tmp_file)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("Template: "+template_path+"\nAcc: " + str(max_val))
        if max_val < threshold: return None

        return max_loc

    @staticmethod
    def locate_all_targets(template_path, threshold=.9):
        targets = []
        template = cv2.imread(template_path)
        h, w = template.shape[:-1]

        # navie method
        tmp_file = os.path.join(config.__TMP__, 'tmp.png')
        pyautogui.screenshot(tmp_file)
        img = cv2.imread(tmp_file)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            targets.append(pt)

        return targets
