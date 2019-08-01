from Pages.hospitalPage import HospitalPage
from utils.DriverUtils import DriverUtils as DriverUtils


class Hospital:

    def __init__(self):
        self.driver = DriverUtils.getDriver()

    def desintoxicar(self):
        hospital = HospitalPage(self.driver)
        try:
            hospital.desintoxicar.click()
        except:
            pass
