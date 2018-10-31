import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetProductListTest(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/products")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        # ("所有参数为空", "", "", "", "", "", "", "", "", 422000, "illegal.request.data", ["date"], ["date"], ["integer"], ["integer"]),
        # ("active_start参数为空", "", "2018-05-11", 1000, 0, "status", "ASC", 1, "", 422000, "illegal.request.data", ["date"], "", "", ""),
        # ("active_end参数为空", "2018-04-26", "", 1000, 0, "status", "ASC", 1, "", 422000, "illegal.request.data", "", ["date"], "", ""),
        # ("status参数为空", "2018-04-26", "2018-05-11", "", 0, "status", "DESC", 1, "", 422000, "illegal.request.data", "", "", ["integer"], ""),
        # ("type参数为空", "2018-04-26", "2018-05-11", 1000, "", None, "DESC", 1, "", 422000, "illegal.request.data", "", "", "", ["integer"]),
        ("type参数为空", "2018-04-26", "2018-05-11", 1000, "", None, "DESC", 1, "", 422000, "illegal.request.data", "", "", "", ["integer"]),


    ])
    def test_get_products_list_null(self, case_name, active_start, active_end,
                                    status, type, sort, order, page, keyword, result_status,
                                    result_message, error_active_start, error_active_end, error_status, error_type,):
        self.payload = {"active_start": active_start, "active_end": active_end, "status": status,
                        "type": type, "sort": sort,
                        "order": order, "page": page, "keyword": keyword}
        r = requests.get(self.url, headers=self.headers, params=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], result_status)
        self.assertEqual(self.result["message"], result_message)
        if case_name == "所有参数为空":
            self.assertEqual(self.result['error']['active_start'], error_active_start)
            self.assertEqual(self.result['error']['active_end'], error_active_end)
            self.assertEqual(self.result['error']['status'], error_status)
            self.assertEqual(self.result['error']['type'], error_type)
        elif case_name == "active_start参数为空":
            self.assertEqual(self.result['error']['active_start'], error_active_start)
        elif case_name == "active_end参数为空":
            self.assertEqual(self.result['error']['active_end'], error_active_end)
        elif case_name == "status参数为空":
            self.assertEqual(self.result["error"]["status"], error_status)
        elif case_name == "type参数为空":
            self.assertEqual(self.result["error"]["type"], error_type)


if __name__ == '__main__':
    # test_data.init_data() # 初始化接口测试数据
    unittest.main()
