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
        ("参数为空", "", "", "", "", "", "", "", "", 422000, "illegal.request.data", ["date"], ["date"], ["integer"],
         ["integer"], ["in"], ["in"], ["integer"]),

    ])
    def test_get_products_list_null(self, case_name, active_start, active_end,
                                    status, type, sort, order, page, keyword, result_status,
                                    result_message, result_error0, result_error1, result_error2, result_error3,
                                    result_error4, result_error5, result_error6, ):
        self.payload = {"active_start": active_start, "active_end": active_end, "status": status,
                        "type": type, "sort": sort,
                        "order": order, "page": page, "keyword": keyword}
        r = requests.get(self.url, headers=self.headers, params=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], result_status)
        self.assertEqual(self.result["message"], result_message)
        self.assertEqual(self.result['error']['active_start'], result_error0)
        self.assertEqual(self.result['error']['active_end'], result_error1)
        self.assertEqual(self.result['error']['status'], result_error2)
        self.assertEqual(self.result['error']['type'], result_error3)
        self.assertEqual(self.result['error']['sort'], result_error4)
        self.assertEqual(self.result['error']['order'], result_error5)
        self.assertEqual(self.result['error']['page'], result_error6)

    @parameterized.expand([
        ("参数为空", "", "", "", "", "", "", "", "", 0, "success", 1),
        ("只传开始日期", "2018-04-01", "", "", "", "", "", "", "", 0, "success", 1),
        ("只传结束日期", "", "2018-04-01", "", "", "", "", "", "", 0, "success", 1),
        ("只选状态0", "", "", "0", "", "", "", "", "", 0, "success", 1),
    ])
    def test_get_product_list_succss(self, case, active_start, active_end, status, type, sort, order, page, keyword,
                                     result_status, message, current_page):
        self.payload = {"active_start": active_start, "active_end": active_end, "status ": status, "type": type,
                        "sort": sort, "order": order, "page": page, "keyword": keyword}
        r = requests.get(self.url, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], result_status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["current_page"], current_page)


if __name__ == '__main__':
    # test_data.init_data() # 初始化接口测试数据
    unittest.main()