# 需求:测试购物车接口， 但是需要先调用登录接口(登录实现比较复杂: 需要录入手机号码， 以及服务器发送的验证码)
# 要求使用 mock 模拟登录功能， 最终， 无论录入什么样的手机号或验证码都能正常登录
# 1、 导包
import unittest
from unittest import mock


# 2、 创建被模拟的接口:登录接口
def login(telphone, verify_code):
    # 复杂实现， 判断验证码是否正确
    # 。 。 。 。
    return False


class TestMyLogin(unittest.TestCase):
    # 测试登录
    def test_login(self):
        # 3、创建mock对象并模拟登录实现
        login = mock.Mock(return_value=True)
        # 4、 调用时， 调用模拟的实现
        result = login("112", "9999")
        print(result)
        # 调用购物车接口 ....
        self.assertEqual(False, result)