import unittest

from case.TestCollections import TestCollections
from case.TestLogin import TestLogin

suite = unittest.TestSuite()
# 组织套件
suite.addTest(TestLogin("test_login_success"))
suite.addTest(TestCollections("test_cancel"))
# 执行
unittest.TextTestRunner().run(suite)