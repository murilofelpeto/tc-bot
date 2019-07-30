from Pages.leftMenuPage import LeftMenuPage
from utils.DriverUtils import DriverUtils as DriverUtils


class LeftMenu:

    def __init__(self):
        self.driver = DriverUtils.getDriver()

    def clickRoubar(self):
        menu = LeftMenuPage(self.driver)
        menu.robberyMenu.click()

    def clickNighClub(self):
        menu = LeftMenuPage(self.driver)
        menu.clubMenu.click()
