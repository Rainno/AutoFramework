# unittest 使用
# 0、 导包
import unittest
import requests


# 1、 创建一个 测试类
class TestTPShop(unittest.TestCase):
    # 三个函数执行前， 需要使用相同的 session 对象
    def setUp(self):
        self.session = requests.session()

    # tearDown 实现资源释放
    def tearDown(self):
        self.session.close()

    # 2、 测试类中编写测试函数
    # 测试1: 获取验证码功能
    def test_get_verify_code(self):
        # 访问获取验证码接口
        response = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print("获取验证码接口的状态码:",response.status_code)
        # 使用断言判断响应结果
        # 状态码是 200
        # 响应头的 Content-Type 包含 image
        status_code = response.status_code
        contentType = response.headers.get("Content-Type")
        #print(status_code)
        #print(contentType)
        self.assertEqual(200,status_code)
        self.assertIn("image",contentType)

    # 测试2: 登录功能
    def test_login(self):
        # 使用 requests 实现登录请求
        # 就执行逻辑而言， 先获取验证码
        self.test_get_verify_code()
        # 再执行登录
        myData = {
            "username":"13012345678",
            "password":"123456",
            "verify_code":"8888"
        }
        response = self.session.post("http://localhost/index.php?m=Home&c=User&a=do_login",data=myData)
        # 断言结果
        status_code = response.status_code
        body = response.json()
        self.assertEqual(200,status_code)
        #self.assertIn("登陆成功",body) # 不能之间将文本与 JSON 对象比对
        self.assertIn("登陆成功",body.get("msg")) # 将文本与 JSON 中提取出的文本信息比对

    # 测试3: 订单查看功能
    def test_order(self):
    # 调用订单查看接口(先登录)
        self.test_login()
        response = self.session.get("http://localhost/Home/Order/order_list.html")
        # 断言判断响应结果
        print("订单:",response.status_code)
        print("订单:",response.text)
        status_code = response.status_code
        body = response.text
        self.assertEqual(200, status_code)
        self.assertIn("<title>我的订单</title>",body)