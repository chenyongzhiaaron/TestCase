import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)


class DelectdeProductPrice(unittest.TestCase):
    def setUp(self):
        self.urlIdNull = global_base.Base.url(self, "/products/prices/{id}")  # 不合法 id
        self.urlIdInvalid = global_base.Base.url(self, "/products/prices/90000")  # id 89893 不存在数据库
        # self.urlIdReleased = global_base.Base.url(self, "/products/739/prices")  # id 739 已上架
        # self.urlIdDisable = global_base.Base.url(self, "/products/588/prices")  # id 588 已下架
        # self.urlIdDraft = global_base.Base.url(self, "/products/781/prices")  # id 781 草稿
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("产品ID不合法", 404000, "request.not.found"),
        ("产品ID不存在数据库", 40000, "request.not.found")
    ])
    def test_delete_product_price(self, case, status, message):
        r = requests.delete(self.urlIdNull, headers=self.header)
        self.result = r.json()
        self.assertEqual(["status"], status)
        self.assertEqual(["message"], message)


if __name__ == "__main__":
    unittest.main()
