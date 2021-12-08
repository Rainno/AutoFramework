import requests

import app


class Channels:
    def __init__(self):
        self.get_channels_url = app.BASE_URL + "app/v1_0/channels"
    def get_channels(self):
        return  requests.get(self.get_channels_url)