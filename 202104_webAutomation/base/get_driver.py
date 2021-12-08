from selenium import webdriver
import page


# 单例模式
class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取driver
            cls.driver = webdriver.Chrome()
            # 最大化
            cls.driver.maximize_window()
            # 打开URL
            cls.driver.get(page.URL)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:  # 确保driver不为空，否则会报错
            cls.driver.quit()
            # 必须置空操作
            cls.driver = None
