import re
import pyautogui

def find_coordinates(self, img):
    """
    Find the given image location

    @params
        img: given image

    @return
        coordinates: (x, y, width, height)
    """
    pass

def keep_numerics(self, text):
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
