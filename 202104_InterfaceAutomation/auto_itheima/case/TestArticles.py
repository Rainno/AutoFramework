import unittest

from api.ArticelsAPI import Articles


class TestArticles(unittest.TestCase):
    def setUp(self):
        self.articles = Articles()

    def test_get_articles_by_channel_id(self):
        response = self.articles.get_articles_by_channel_id(2)
        self.assertEqual("OK", response.json().get("message"))