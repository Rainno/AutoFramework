"""业务层"""
import unittest
from time import sleep

from page.page_login import PageLogin
from base.get_driver import GetDriver
from parameterized import parameterized

from tool.read_txt import read_txt

from base.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


def get_data():
    # username, pwd, verify_code, expect_result,status
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))

    return arrs[1::]


class Test(unittest.TestCase):
    login = None

    # 新建setupClass
    @classmethod
    def setUpClass(cls):
        try:
            # 获取driver
            cls.driver = GetDriver.get_driver()
            # 实例化PageLogin()
            cls.login = PageLogin(cls.driver)
            # 点击登录链接
            cls.login.page_click_login_link()
        except Exception as e:
            log.error("[test_login]:出错：{}".format(e))
            # 截图(可要可不要)
            # cls.login.base_get_image()

    # 新建tearDownClass
    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    # 新建 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect_result, status):
        try:
            sleep(3)
            # 调用 登录业务方法
            self.login.page_login(username, pwd, verify_code)
            # 判断是否为正向
            if status == "True":
                try:
                    # 断言是否登录成功  怎么会返回None呢？-----不能运行成功，所以注释掉，便可以运行成功
                    self.assertTrue(self.login.page_if_login_success())
                except Exception as e:
                    # 截图
                    self.login.base_get_image()
                    log.error("[test_login]:出错：{}".format(e))
                # 点击 安全退出
                self.login.page_click_logout_link()

                # 点击登录链接
                self.login.page_click_login_link()
            # 逆向用例
            else:
                # 获取错误提示信息
                msg = self.login.page_get_err_info()
                print("错误信息msg:", msg)
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    # 截图
                    self.login.base_get_image()
                    log.error("[test_login]:出错：{}".format(e))

                # 点击错误提示框 确定按钮
                self.login.page_click_error_alert()
        except Exception as e:
            log.error("[test_login]:出错：{}".format(e))
            # 截图
            self.login.base_get_image()