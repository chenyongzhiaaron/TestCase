import unittest
import requests
import os
import sys
from ProductManagement import global_base
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from parameterized import parameterized


class GetProductRecordsTest(unittest.TestCase):

    ''' 获取产品操作记录 '''

    def setUp(self):
        self.base_url = global_base.BaseUrl.url(self, "/products/739/records")
        self.headers = global_base.BaseUrl.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("page_min-1", 0, 422000, "illegal.request.data", ["min|number|1"]),
        ("page_max+1", 100000000, 422000, "illegal.request.data", ["max|number|99999999"]),
        ("page_字母", "abc", 422000, "illegal.request.data", ["integer"]),
        ("page_中文", "abc", 422000, "illegal.request.data", ["integer"]),
        ("page_特殊符号", "//&\\", 422000, "illegal.request.data", ["integer"]),
        ("page_null", "abc", 422000, "illegal.request.data", ["integer"]),

    ])
    def test_get_product_records_illegal(self, case_name, page, status, message, error_page):
        self.params = {"page": page}
        r = requests.get(self.base_url, headers=self.headers, params=self.params)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result['message'], message)
        self.assertEqual(self.result['error']["page"], error_page)

    @parameterized.expand([
        ('page_min', 1, 0, "success", 1, "Aaron"),
        ('page_min+1', 2, 0, "success", 2, "Aaron"),

    ])
    def test_get_product_records_success(self, case_name, page, status, message, result_data01, result_data02, ):
        self.params = {"page": page}
        r = requests.get(self.base_url, headers=self.headers, params=self.params)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["current_page"], result_data01)
        self.assertEqual(self.result["data"]['data'][0]['user_name'], result_data02)

@parameterized.expand([
    ('page_max', 99999999, 0, "success", 99999999, "[]", "null", 2),
    ('page_max-1', 99999998, 0, "success", 99999998, "[]", "null", 2),

])
def test_get_product_records_success(self, case_name, page, status, message, result_data01, result_data02, result_data03,
                                     result_data04):
    params = {"page": page}
    r = requests.get(self.base_url, headers=self.headers, params=params)
    self.result = r.json()
    self.assertEqual(self.result["status"], status)
    self.assertEqual(self.result["message"], message)
    self.assertEqual(self.result["data"]["current_page"], result_data01)
    self.assertEqual(self.result["data"]['data']['data'], result_data02)
    self.assertEqual(self.result["data"]['data']['from'], result_data03)
    self.assertEqual(self.result["data"]['data']['last_page'], result_data04)


if __name__ == '__main__':
    # test_data.init_data() # 初始化接口测试数据
    unittest.main()
