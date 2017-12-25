import app.config as config

from app.scripts.utils import FindCoordinates
from app.scripts.autocontroller import AutoController
from app.scripts.autocheck import AutoCheck

class Robot(object):

    def __init__(self):
        self.checker = AutoCheck()
        pass

    def run(self):
        """
        SOP
        1. Select Weapons/Cards menu...
        2. Choose type of Weapons/Cards...
        3. Get all price selected target
        """

        print("START RUN")
        # select menu
        for equid in config.MENU_LIST:
            success = self._select_for_image(equid)
            if success is False: continue
            # select subitems of selected item
            for baseline in config.EQUID_BASELINE_LIST:
                base = FindCoordinates.locate_target(baseline)
                if base is None: continue
                for ix, item_list in enumerate(config.EQUID_LIST):
                    anchor = (base[0], base[1]+ix*config.EQUID_STEP_SIZE)
                    self._select_for_anchor(anchor)

                    for item in item_list:
                        success = self._select_for_image(item)
                        print('SELECT '+item + ':'+str(success))

                        print(self.checker.get_all_price())
        pass

    def _select_for_image(self, img_path):
        coords = FindCoordinates.locate_target(img_path)

        return AutoController.click(coords)

    def _select_for_anchor(self, anchor):
        """
        Select the menu/item for anchor

        @params:
            img_path: the path of image you want to select
        """
        print("Success: " + str(AutoController.click(anchor)))
        pass

    def _get_price_for_item(self):
        """
        """
        pass
