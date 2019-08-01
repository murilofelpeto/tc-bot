from Pages.loginPage import LoginPage
from utils.DriverUtils import DriverUtils as DriverUtils


class Login:

    def __init__(self):
        self.cookies_dict = dict()

    def doLogin(self):
        DriverUtils.selecionaBrowser()
        driver = DriverUtils.getDriver()
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.get('https://www.thecrims.com')

        login = LoginPage(driver)
        login.username = 'MrCheater'
        login.password = "23e33913f208"
        login.submit.click()
