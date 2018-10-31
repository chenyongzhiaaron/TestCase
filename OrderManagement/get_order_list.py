import unittest

import requests
from parameterized import parameterized

from OrderManagement import global_base


class OrderList(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/orders")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("正确url验证获取数据成功", 0, "success", 1)
    ])
    def test_get_order_list(self, case, status, message, data_current_page):
        self.result = requests.get(self.url, headers=self.headers).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["current_page"], data_current_page)


if __name__ == "__main__":
    unittest.main()
