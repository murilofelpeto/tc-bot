import re
import time
from Pages.rightMenuPage import RightMenuPage
from utils.DriverUtils import DriverUtils as DriverUtils


class RightMenu:

    def __init__(self):
        self.stamina = []
        self.vicio = []
        self.respeito = []
        self.driver = DriverUtils.getDriver()

    def getStamina(self):
        time.sleep(0.7)
        rightMenu = RightMenuPage(self.driver)
        staminaText = rightMenu.stamina.text
        self.stamina = re.findall('\d+', staminaText)
        return self.stamina[0]

    def getVicio(self):
        time.sleep(0.7)
        rightMenu = RightMenuPage(self.driver)
        vicioText = rightMenu.vicio.text
        self.vicio = re.findall('\d+', vicioText)
        return self.vicio[0]

    def getRespeito(self):
        time.sleep(0.7)
        rightMenu = RightMenuPage(self.driver)
        respeitoText = rightMenu.respeito.text
        self.respeito = re.findall('\d+', respeitoText)
        return self.respeito[0]

