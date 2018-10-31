import unittest

import requests
from parameterized import parameterized

from OrderManagement import global_base


class UpdateOrderRemark(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/order/307/remark")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("参数为空", 0, "success")
    ])
    def test_update_order_remark(self, case, status, message, data_current_page):
        self.result = requests.get(self.url, headers=self.headers).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["current_page"], data_current_page)


if __name__ == "__main__":
    unittest.main()
