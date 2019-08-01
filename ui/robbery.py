import re
import time
from collections import OrderedDict

from selenium.webdriver.support.select import Select

from Pages.robberyPage import RobberyPage
from utils.DriverUtils import DriverUtils as DriverUtils


class Robbery:

    def __init__(self, stamina):
        self.stamina = stamina
        self.robberMap = dict()
        self.driver = DriverUtils.getDriver()

    def doRobbery(self):
        time.sleep(1)
        robbery = RobberyPage(self.driver)
        self.robberMap = self.getRobberList(Select(robbery.robberySelect))
        self.selectRobbery(self.stamina, Select(robbery.robberySelect))
        robbery.robberyButton.click()

    def getRobberList(self, robberySelect):
        robberyMap = dict()
        for item in robberySelect.options:
            value = item.text.replace("%", " ")
            value = value.replace(" ", "")
            key = 0 if (item.get_attribute("value") == '') else int(
                item.get_attribute("value"))
            robberyMap.update({key: value})
        return robberyMap

    def selectRobbery(self, stamina, robberySelect):
        orderedRobberMap = OrderedDict(sorted(self.robberMap.items(), key=lambda k: k, reverse=True))
        for key in orderedRobberMap.keys():
            numbers = re.findall('\d+', orderedRobberMap[key])
            staminaGasta = int(numbers[0])
            chanceSucesso = int(numbers[1])
            if (stamina >= staminaGasta) and (chanceSucesso == 100):
                robberySelect.select_by_value(str(key))
                break
