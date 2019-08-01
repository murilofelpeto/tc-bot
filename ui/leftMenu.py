from Pages.leftMenuPage import LeftMenuPage
from utils.DriverUtils import DriverUtils as DriverUtils
import time

class LeftMenu:

    def __init__(self):
        self.driver = DriverUtils.getDriver()

    def clickRoubar(self):
        menu = LeftMenuPage(self.driver)
        url = menu.w.current_url
        if "robberies" not in url:
            menu.robberyMenu.click()

    def clickNighClub(self):
        time.sleep(0.5)
        menu = LeftMenuPage(self.driver)
        menu.clubMenu.click()

    def clickHospital(self):
        time.sleep(0.5)
        menu = LeftMenuPage(self.driver)
        menu.hospitalMenu.click()
