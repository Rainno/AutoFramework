# 组织测试套件, 先登录， 然后再收藏
# 注意：要先修改TestCase中文件读取文件的路径，使用绝对路径而非相对路径
# 1、导入unittest
import unittest
# 2、创建suite 对象
from case.TestCollections import TestCollections
from case.TestLogin import TestLogin

suite = unittest.TestSuite()

# 3、suite 添加被执行的操作
suite.addTest(TestLogin("test_login_success"))
suite.addTest(TestCollections("test_save"))

# 4、最后执行suite
unittest.textTestRunner().run(suite)