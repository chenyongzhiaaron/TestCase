import os
import sys
import unittest

import requests

from RepositoryManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class Repositories(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/repositories")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    def test_get_repositories(self):
        r = requests.get(self.url, headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result["status"], 0)
        self.assertEqual(self.result["message"], "success")


if __name__ == "__main__":
    unittest.main()
