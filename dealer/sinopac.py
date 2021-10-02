import os
from time import sleep
import pyautogui

from utils.process import check_is_running

desktop_path = os.path.expanduser("~/Desktop")


class SinoPac:

    def __init__(self, password=''):
        self.password = password

    def launch_sfuture_trader(self):
        if not check_is_running('SFT.exe'):
            app = desktop_path + '\\' + 'SFutureTrader.appref-ms'
            os.system(app)

            sleep(3)

            # input password
            pyautogui.press(keys='tab', presses=3, interval=0.5)
            pyautogui.typewrite(self.password)
            pyautogui.press('enter')

            return True

        return False

    def launch_eleader(self):
        if not check_is_running('Meow.exe'):
            app = 'C:\\eleader\\bin\\VUp2.exe'
            os.system(app)

            sleep(1)
            # input password
            pyautogui.typewrite(self.password)
            pyautogui.press('enter')

            return True

        return False

    def launch_vip(self):
        if not check_is_running('ITS.exe'):
            app = desktop_path + '\\永豐金證券VIP閃電.lnk'
            os.system(app)
            sleep(20)
            pyautogui.press('tab')
            pyautogui.press('enter')

    def launch_xq(self):
        if not check_is_running('daqSINOAP.exe'):
            app = 'C:\\SINOAP\\daqSINOAP.exe'
            os.system(app)
            return True
        return False
