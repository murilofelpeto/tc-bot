from ui.login import Login
from ui.rightMenu import RightMenu
from ui.robbery import Robbery
from ui.leftMenu import LeftMenu
from ui.nightClub import NightClub
from ui.hospital import Hospital

login = Login()
login.doLogin()
rightMenu = RightMenu()
leftMenu = LeftMenu()

while True:
    stamina = int(rightMenu.getStamina())
    if stamina >= 5:
        leftMenu.clickRoubar()
        robbery = Robbery(stamina)
        robbery.doRobbery()
    else:
        vicio = int(rightMenu.getVicio())
        if vicio >= 3:
            leftMenu.clickHospital()
            hospital = Hospital()
            hospital.desintoxicar()
        else:
            respeito = int(rightMenu.getRespeito())
            leftMenu.clickNighClub()
            nightClub = NightClub()
            nightClub.enterWhoreHouse(respeito)
            nightClub.pickWhore()