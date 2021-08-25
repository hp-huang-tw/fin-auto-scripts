import requests
import logging


class LineNotify:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def send_text(self, text):
        params = {
            "message": text
        }
        r = requests.post("https://notify-api.line.me/api/notify", headers=self.headers, params=params)

        if r.status_code != 200:
            logging.error("send line notify failed. result: " + r.json())
