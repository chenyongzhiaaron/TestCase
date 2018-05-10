import os
import sys
import unittest

import requests
from parameterized import parameterized

from StatisticsManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetTmallSalesDate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/sales")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("输入正确的日期获取数据成功", "2018-04-01", "2018-04-01", 0, "success"),
    ])
    def test_get_tmall_sales_date(self, case, date_start, data_end, status, message):
        payload = {"date_start": date_start, "date_end": data_end}
        r = requests.get(self.url, headers=self.header, params=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    unittest.main()
