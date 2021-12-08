import requests

import app


class Collection:
    def __init__(self):
        self.collections_url = app.BASE_URL + "app/v1_0/article/collections"
        #self.collections_cancel_url = app.BASE_URL + "app/v1_0/article/collections/"

    # 收藏
    def save(self, id, token):
        myJson = {"target": id}
        # 获取token后要提交
        # 需要设置信息头:{"Content-Type":"application/json","Authorization":"Bearer TOKEN的值"}
        myHeader = {
            "Content-Type":"application/json",
            "Authorization":"Bearer" + token
        }
        return requests.post(self.collections_url, json=myJson, headers=myHeader)

    # 取消收藏
    def cancel(self, id, token):
        myHeader = {
            "Content-Type": "application/json",
            "Authorization": "Bearer" + token
        }
        return requests.delete(self.collections_url + "/" + id, headers = myHeader)