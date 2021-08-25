import os
from time import sleep
import pyautogui

from utils.process import check_is_running

desktop_path = 'C:\\Users\\User\\Desktop'

class EnTrust:

    def launch_vip_trading_system(self):
        if not check_is_running('VIPTradingSystem.exe'):
            app = desktop_path + '\\' + '華南雷神Super.appref-ms'
            os.system(app)

            sleep(1)

            pyautogui.press('enter')
            return True

        return False
