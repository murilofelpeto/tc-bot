import re

from Pages.rightMenuPage import RightMenuPage
from utils.DriverUtils import DriverUtils as DriverUtils


class RightMenu:

    def __init__(self):
        self.stamina = []
        self.vicio = []
        self.driver = DriverUtils.getDriver()

    def getStamina(self):
        rightMenu = RightMenuPage(self.driver)
        staminaText = rightMenu.stamina.text
        self.stamina = re.findall('\d+', staminaText)
        return self.stamina[0]

    def getVicio(self):
        rightMenu = RightMenuPage(self.driver)
        vicioText = rightMenu.vicio.text
        self.vicio = re.findall('\d+', vicioText)
        return self.vicio[0]
