from time import sleep
import os
from dotenv import load_dotenv

from dealer.sinopac import SinoPac
from dealer.entrust import EnTrust

from notify.line_notify import LineNotify


if __name__ == '__main__':
    load_dotenv()

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
