from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverUtils:

    driver = webdriver

    def selecionaBrowser():
        DriverUtils.driver = webdriver.Chrome(ChromeDriverManager().install())
       
    def getDriver():
        return DriverUtils.driver
