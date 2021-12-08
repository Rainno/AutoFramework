import  unittest

from api.ChannelsAPI import Channels


class TestChannels(unittest.TestCase):
    def setUp(self):
        self.channels = Channels()
    # 编写获取频道列表的测试函数
    # 1、无提交的测试数据，不需设置data
    # 2、需要调用api实现
    def test_get_channels(self):
        response = self.channels.get_channels()
        # 判断断言
        self.assertEqual("OK", response.json().get("message"))