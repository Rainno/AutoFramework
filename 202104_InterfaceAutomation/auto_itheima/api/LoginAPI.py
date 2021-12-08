import requests
import app


class Login:

    def __init__(self):
        self.get_verify_code_url = app.BASE_URL + "app/v1_0/sms/codes/"
        self.login_url = app.BASE_URL + "app/v1_0/authorizations"
    # 1、获取验证码
    def get_verify_code(self, mobile):
        return requests.get(self.get_verify_code_url + mobile)

    # 2、登录函数
    def login(self,mobile, code):
        myJson = {}
        if mobile:
            myJson["mobile"] = mobile
        if code:
            myJson["code"] = code
        return requests.post(self.login_url, json = myJson)