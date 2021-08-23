import os
from time import sleep

import psutil

desktop_path = 'C:\\Users\\User\\Desktop'


def check_is_running(name):
    return name in (p.name() for p in psutil.process_iter())


def launch_sfuture_trader():
    if not check_is_running('SFT.exe'):
        app = desktop_path + '\\' + 'SFutureTrader.appref-ms'
        os.system(app)


def launch_vip_trading_system():
    if not check_is_running('VIPTradingSystem.exe'):
        app = desktop_path + '\\' + '華南雷神Super.appref-ms'
        os.system(app)


def launch_eleader():
    if not check_is_running('Meow.exe'):
        app = 'C:\\eleader\\bin\\VUp2.exe'
        os.system(app)


if __name__ == '__main__':
    launch_sfuture_trader()

    sleep(1)
    launch_vip_trading_system()

    sleep(1)
    launch_eleader()
