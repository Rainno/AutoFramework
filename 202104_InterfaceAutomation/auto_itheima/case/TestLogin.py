# 搭框架
# 1、导包
import json
import unittest
from parameterized import parameterized

import app
from api.LoginAPI import Login


# 读取json数据
def read_from_json():
    data = []
    with open(app.ABS_DIR + "/data/login_case.json", "r", encoding="utf-8") as f:
        vs = json.load(f).values() # 获取所有值
        for v in vs:
            mobile = v.get("mobile")
            code = v.get("code")
            status_code = v.get("status_code")
            message = v.get("message")
            case_one = (mobile, code, status_code, message)
            data.append(case_one)
    print(data)
    return data


# 2、创建测试类


class TestLogin(unittest.TestCase):
    # 3、创建测试函数，测试登录
    def setUp(self):
        self.login = Login()

    # 函数1： 获取短信验证码
    # 只需要提交正确手机号码即可
    def test_get_verify_code(self):
        # 调用api实现
        response = self.login.get_verify_code("18883504534")
        print(response.json())

    # 函数2：测试登录
    # 参数化导入data的测试数据
    @parameterized.expand(read_from_json())
    def test_login(self, mobile, code, status_code, message):
        # 调用api实现
        response = self.login.login(mobile, code)
        # 断言判断
        # 判断状态
        self.assertEqual(status_code, response.status_code)
        # 判断响应体
        self.assertIn(message, response.text)

    def test_login_success(self):
        response = self.login.login("18883504534", "")
        # 提取token
        token = response.json().get("data").get("token")
        # 将Token传递到公共空间app.py
        app.TOKEN = token
        self.assertEqual(201, response.status_code)
        self.assertIn("OK", response.text)
