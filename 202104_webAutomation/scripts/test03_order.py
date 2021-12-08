import unittest
from time import sleep
from selenium.common.exceptions import UnexpectedAlertPresentException

from base.get_driver import GetDriver
from page.page_order import PageOrder
from page.page_login import PageLogin
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class TestOrder(unittest.TestCase):

    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化pageorder
        self.order = PageOrder(self.driver)
        # 调用登录PageLogin对象中，登录方法
        PageLogin(self.driver).page_login_success()
        # 回到首页
        self.order.page_click_index()
        # 此处该方法跳不到首页，不可行
        # self.order.base_index()

    def tearDown(self):
        GetDriver.quit_driver()

    # 订单测试方法
    def test_order(self):
        try:
            self.order.page_order(self.driver)
            # 断言
            msg = self.order.page_get_submit_result()
            print("msg:", msg)
            self.assertIn("提交成功", msg)
        except Exception as e:
            log.error("[test_cart]:出错：{}".format(e))
            # 截图
            self.order.base_get_image()
