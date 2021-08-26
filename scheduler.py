import time
import schedule
from schedule import every, repeat

from launch_order import OrderLauncher

eight_clock = "08:00"


@repeat(every().monday.at(eight_clock))
@repeat(every().tuesday.at(eight_clock))
@repeat(every().wednesday.at(eight_clock))
@repeat(every().thursday.at(eight_clock))
@repeat(every().friday.at(eight_clock))
def launch_order():
    OrderLauncher().launch()


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
