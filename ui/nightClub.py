from Pages.nightClubPage import NightClubPage
from utils.DriverUtils import DriverUtils as DriverUtils
from selenium import webdriver

import time
import re

class NightClub:

    def __init__(self):
        self.driver = DriverUtils.getDriver()

    def enterWhoreHouse(self, respeito):
        tentativas = 0
        while tentativas < 2:
            try:
                time.sleep(0.2)
                nightClub = NightClubPage(self.driver)
                nightClub.whoreHouseTab.click()

                for whorehouse in nightClub.whorehouses:
                    try:
                        time.sleep(0.4)
                        tableBody = whorehouse.find_element_by_tag_name("tbody")
                        tableRow = tableBody.find_elements_by_tag_name("tr")
                        respectTableColumn = tableRow[1]
                        respectMin = self.getRespect(respectTableColumn, 'Min')
                        respectMax = self.getRespect(respectTableColumn, 'Max')
                        if (respeito >= respectMin) and (respeito <= respectMax):
                            enterButton = tableBody.find_element_by_tag_name("button")
                            enterButton.click()
                            break
                    except:
                        pass
            except:
                pass
            tentativas = tentativas + 1
        
    def pickWhore(self):
        tentativas = 0
        while tentativas < 2:
            try:
                nightClub = NightClubPage(self.driver)
                tableBody = nightClub.whores.find_element_by_tag_name("tbody")
                tableRow = tableBody.find_elements_by_tag_name("tr")
                for line in tableRow:
                    colunas = line.find_elements_by_tag_name("td")
                    if 'Miss Blonde' in colunas[0].text:
                        line.find_element_by_xpath("//button[@class='btn btn-inverse btn-small']").click()
                        break
            except:
                pass
            tentativas = tentativas + 1

    def exitWhoreHouse(self):
        nightClub = NightClubPage(self.driver)
        nightClub.exit.click()

    
    def getRespect(self, respectColumn, texto):
        done = False
        tentativas = 0
        while tentativas < 2:
            try:
                respeitoText = respectColumn.find_element_by_xpath("//div[contains(text(), " + texto + ")]")
                respeito = re.findall('\d+', respeitoText.text)
            except:
                pass
            tentativas = tentativas + 1
        
        if len(respeito) == 0:
            if texto in 'Min':
                return 0
            else:
                return 999999999
        else:
            return int(respeito[0])
        