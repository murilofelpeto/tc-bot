from ui.login import Login
from ui.rightMenu import RightMenu
from ui.robbery import Robbery
from ui.leftMenu import LeftMenu

login = Login()
login.doLogin()
rightMenu = RightMenu()
leftMenu = LeftMenu()

stamina = int(rightMenu.getStamina())
if stamina >= 5:
    leftMenu.clickRoubar()
    robbery = Robbery(stamina)
    robbery.doRobbery()
else:
    #Recuperar stamina
    if int(rightMenu.getVicio) >= 3:
        #Hospital
    else:
        leftMenu.clickNighClub()