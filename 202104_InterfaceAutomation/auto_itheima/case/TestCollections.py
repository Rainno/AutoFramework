import unittest

import app
from api.ArticelsAPI import Articles
from api.CollectionAPI import Collection


class TestCollections(unittest.TestCase):
    def setUp(self):
        self.collection = Collection()

    def test_save(self):
        # 传入收藏的文章id
        response = self.collection.save(1, app.TOEKN)
        self.assertEqual("OK", response.json().get("message"))

    def test_cancel(self):
        response = self.collection.cancel("1", app.TOEKN)
        self.assertEqual(204, response.status_code)