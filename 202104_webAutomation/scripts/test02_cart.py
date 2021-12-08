import unittest
from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


# 定义测试类
class TestCart(unittest.TestCase):
    def setUp(self):
        try:
            # 获取driver
            self.driver = GetDriver().get_driver()
            # 实例化PageCart页面
            self.cart = PageCart(self.driver)
            # 调用成功登录  依赖
            PageLogin(self.driver).page_login_success()
            # 跳转到首页
            self.cart.page_open_index()
        except Exception as e:
            log.error("[test_cart]:出错：{}".format(e))
            # 截图(可要可不要)
            self.cart.base_get_image()

    def tearDown(self):
        GetDriver().quit_driver()

    # 定义测试购物车方法
    def test_add_cart(self):
        # 调用  组合添加购物车业务方法
        self.cart.page_add_cart()
        # 断言是否添加成功
        msg = self.cart.page_get_text()
        print("msg:", msg)
        try:
            self.assertEqual(msg, "添加成功")
        except Exception as e:
            log.error("[test_cart]:出错：{}".format(e))
            # 截图
            self.cart.base_get_image()
        # 关闭窗口
        self.cart.page_close_window()
