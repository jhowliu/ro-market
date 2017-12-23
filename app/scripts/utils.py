import re
import pyautogui

from PIL import Image

def find_coordinates(img_path):
    """
    Find the given image location

    @params
        img: given image

    @return
        coordinates: (x, y)
    """
    target = pyautogui.locateCenterOnScreen(Image.open(img_path))
    if target is None: return None

    return (target[0], target[1])

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
