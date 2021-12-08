import requests

import app


class Articles:
    def __init__(self):
        self.get_articles_by_channel_id_url = app.BASE_URL + "app/v1_0/articles"

    def get_articles_by_channel_id(self, channel_id):
        myParams = {"channel_id": channel_id}
        return requests.get(self.get_articles_by_channel_id_url, params=myParams)