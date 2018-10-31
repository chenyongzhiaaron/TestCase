import unittest

import requests
from parameterized import parameterized

from RepositoryManagement import global_base


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/products/orders")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("所有参数为空", "", "", "", 422000, "illegal.request.data", ["required"], ["required"], ["required"]),
        ("输入参数不合法", "", "", "", 422000, "illegal.request.data", ["required"], ["required"], ["required"]),
        ("输入参数不存在", "", "", "", 422000, "illegal.request.data", ["required"], ["required"], ["required"]),
        ("输入参数为null", "", "", "", 422000, "illegal.request.data", ["required"], ["required"], ["required"]),
        ("输入参数正确，返回成功响应", 105, 104, 305, 0, "success", ["required"], ["required"], ["required"]),
    ])
    def test_repository_order_product_list(self, case, outgoing_repository_id, incoming_repository_id, order_id, status,
                                           message,
                                           error_outgoing_repository_id, error_incoming_repository_id, error_order_id):
        self.params = {"outgoing_repository_id": outgoing_repository_id,
                       "incoming_repository_id": incoming_repository_id, "order_id": order_id}
        r = requests.get(self.url, headers=self.headers, params=self.params)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    unittest.main()
