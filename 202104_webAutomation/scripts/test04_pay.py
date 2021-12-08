import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay
from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class TestPay(unittest.TestCase):
    def setUp(self):
        self.driver = GetDriver().get_driver()
        self.pay = PagePay(self.driver)
        PageLogin(self.driver).page_login_success()
        # 此处该方法可以跳到首页，可行
        self.pay.base_index()

    def tearDown(self):
        GetDriver().quit_driver()

    def test_pay(self):
        try:
            # 调用支付方式
            self.pay.page_pay()
            # 断言
            self.assertIn("订单提交成功", self.pay.page_get_payment_result())
        except Exception as e:
            # 日志
            log.error("[test_cart]:出错：{}".format(e))
            # 截图
            self.pay.base_get_image()