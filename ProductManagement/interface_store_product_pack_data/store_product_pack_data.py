import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)


class DeletedProduct(unittest.TestCase):
    def setUp(self):
        self.urlIdNull = global_base.Base.url(self, "/products/{id}/packs")  # 不合法 id
        self.urlIdInvalid = global_base.Base.url(self, "/products/89893/packs")  # id 89893 不存在数据库
        self.urlIdReleased = global_base.Base.url(self, "/products/739/packs")  # id 739 已上架
        self.urlIdDisable = global_base.Base.url(self, "/products/588/packs")  # id 588 已下架
        self.urlIdDraft = global_base.Base.url(self, "/products/781/packs")  # id 781 草稿
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("验证ID不合法，请求失败", 404000, "request.not.found"),
    ])
    def test_store_prodcut_pack_null(self, case, status, message):
        r = requests.post(self.urlIdNull, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("验证ID不存在数据库，修改失败", 422000, "illegal.request.data", ['required']),
    ])
    def test_store_product_pack_invalid(self, case, status, message, error):
        r = requests.post(self.urlIdInvalid, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["error"]["packs"], error)


if __name__ == "__main__":
    unittest.main()
