from time import sleep
import datetime
import os
from dotenv import load_dotenv

from dealer.sinopac import SinoPac
from dealer.entrust import EnTrust

from notify.line_notify import LineNotify
from sreenshot import take_screenshot


def screenshot():
    screenshot_dir = os.getenv('SCREENSHOT_DIR')

    now = datetime.datetime.now()
    now_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = screenshot_dir + now_string + '.png'
    take_screenshot(filename)

    line_notify_token = os.getenv('LINE_NOTIFY_TOKEN')
    line_notify_client = LineNotify(line_notify_token)
    line_notify_client.send_image('Order programs are launched at ' + now_string, filename)


class OrderLauncher:

    def __init__(self):
        load_dotenv()

    def launch(self):
        sinopac_password = os.getenv('SINOPAC_PASSWORD')
        line_notify_token = os.getenv('LINE_NOTIFY_TOKEN')

        line_notify_client = LineNotify(line_notify_token)

        sinopac = SinoPac(sinopac_password)

        if sinopac.launch_sfuture_trader():
            line_notify_client.send_text("sfuture_trader is launched.")

        sleep(1)
        if sinopac.launch_eleader():
            line_notify_client.send_text("eleader is launched.")

        sleep(1)
        entrust = EnTrust()
        if entrust.launch_vip_trading_system():
            line_notify_client.send_text("entrust vip is launched.")

        sleep(5)
        screenshot()


if __name__ == '__main__':
    launcher = OrderLauncher()
    launcher.launch()
