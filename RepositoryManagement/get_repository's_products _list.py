import unittest

import requests
from parameterized import parameterized

from RepositoryManagement import global_base


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/products")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("出入仓库存在且有共同产品", 105, 104, 0, "success", "", ""),
        ("出入仓库存在且没有共同产品", 100, 104, 0, "success", ['exists'], ['exists']),
        ("出入仓库都不存在", 999, 1000, 422000, "illegal.request.data", ["exists"], ["exists"]),
        ("出库仓库存在，入库仓库不存在", 105, 1000, 422000, "illegal.request.data", "", ["exists"]),
        ("出库仓库不存在，入库仓库存在", 999, 100, 422000, "illegal.request.data", "", ["exists"]),
        ("出入仓库相同", 105, 105, 422000, "illegal.request.data", "", ["different"]),
        ("出入仓库参数为空", "", "", 422000, "illegal.request.data", ["required"], ["required"]),
        ("出入仓库参数为string", "ab、\c", "我是谁", 422000, "illegal.request.data", ["integer"], ["integer"]),
        ("出入仓库参数为null", "null", "null", 422000, "illegal.request.data", ["integer"], ['different', 'integer']),
    ])
    def test_repository_products(self, case, outgoing_repository_id, incoming_repository_id, status, message,
                                 error_outgoing_repository_id, error_incoming_repository_id):
        self.params = {"outgoing_repository_id": outgoing_repository_id,
                       "incoming_repository_id": incoming_repository_id}
        r = requests.get(self.url, headers=self.headers, params=self.params)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        if case == "出入仓库都不存在":
            self.assertEqual(self.result["error"]["outgoing_repository_id"], error_outgoing_repository_id)
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
        elif case == "出库仓库存在，入库仓库不存在":
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
        elif case == "出库仓库不存在，入库仓库存在":
            self.assertEqual(self.result["error"]["outgoing_repository_id"], error_incoming_repository_id)
        elif case == "出入仓库相同":
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
        elif case == "出入仓库参数为空":
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
        elif case == "出入仓库参数为string":
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
        elif case == "出入仓库参数为null":
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)
            self.assertEqual(self.result["error"]["incoming_repository_id"], error_incoming_repository_id)

if __name__ == '__main__':
    unittest.main()
