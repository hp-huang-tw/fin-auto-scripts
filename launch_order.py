from time import sleep
import datetime
import os
from dotenv import load_dotenv

from dealer.sinopac import SinoPac
from dealer.entrust import EnTrust

from notify.line_notify import LineNotify
from sreenshot import take_screenshot
from utils.keyborad_detector import get_capslock_state, disable_capslock


def screenshot():
    screenshot_dir = os.getenv('SCREENSHOT_DIR')

    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = screenshot_dir + now_string + '.png'
    take_screenshot(filename)

    line_notify_token = os.getenv('LINE_NOTIFY_TOKEN')
    line_notify_client = LineNotify(line_notify_token)
    line_notify_client.send_image('Order programs are launched at ' + now_string, filename)


class SoftwareLauncher:

    def __init__(self):
        load_dotenv()
        self.line_notify_client = LineNotify(os.getenv('LINE_NOTIFY_TOKEN'))
        self.sinopac = SinoPac(os.getenv('SINOPAC_PASSWORD'))
        self.entrust = EnTrust()

    def launch_order_programs(self):
        if self.sinopac.launch_sfuture_trader():
            self.line_notify_client.send_text("sfuture_trader is launched.")

        # replace eleader with vip
        # sleep(1)
        # if self.sinopac.launch_eleader():
        #     self.line_notify_client.send_text("eleader is launched.")

        sleep(1)

        if self.entrust.launch_vip_trading_system():
            self.line_notify_client.send_text("entrust vip is launched.")

        sleep(1)
        if self.sinopac.launch_vip():
            self.line_notify_client.send_text("vip is launched.")

        sleep(5)
        screenshot()

    def launch_xq(self):
        # xq can detect pyautogui, so do nothing after launching it...
        self.sinopac.launch_xq()


if __name__ == '__main__':
    CAPSLOCK = get_capslock_state()
    if CAPSLOCK:
        print("WARNING:  CAPS LOCK IS ENABLED!")
        disable_capslock()

    launcher = SoftwareLauncher()
    launcher.launch_order_programs()
    launcher.launch_xq()
