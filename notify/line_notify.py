import requests
import logging


class LineNotify:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": "Bearer " + self.token
        }

    def send_text(self, text):
        params = {
            "message": text
        }
        r = requests.post("https://notify-api.line.me/api/notify", headers=self.headers, params=params)

        if r.status_code != 200:
            logging.error("send line notify failed. result: " + r.json())

    def send_image(self, text, image_file):
        params = {
            "message": text
        }

        files = {'imageFile': open(image_file, 'rb')}

        r = requests.post("https://notify-api.line.me/api/notify", headers=self.headers, params=params, files=files)

        if r.status_code != 200:
            logging.error("send line notify failed. result: " + r.json())
