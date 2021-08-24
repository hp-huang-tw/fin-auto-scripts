from time import sleep
import os
from dotenv import load_dotenv

from dealer.sinopac import SinoPac
from dealer.entrust import EnTrust


if __name__ == '__main__':
    load_dotenv()
    sinopac_password = os.getenv('SINOPAC_PASSWORD')

    sinopac = SinoPac(sinopac_password)
    sinopac.launch_sfuture_trader()

    sleep(1)
    sinopac.launch_eleader()

    sleep(1)
    entrust = EnTrust()
    entrust.launch_vip_trading_system()
