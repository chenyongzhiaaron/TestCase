import os
import sys
import unittest

import requests
from parameterized import parameterized

from StatisticsManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetTmallBrowseData(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/purpose")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("日期参数正确(当前天)", "2018-04-01", "2018-04-01", 0, "success", "2018-04-01", "41965.0000000000", "1794.0000000000",
         "1413765.0000000000",
         "40171.0000000000", "", "", "", "", ""),
        ("日期参数正确(两天)", "2018-04-01", "2018-04-02", 0, "success", "2018-04-01", "41965.0000000000", "1794.0000000000",
         "1413765.0000000000",
         "40171.0000000000", "2018-04-02", "23524.0000000000", "1196.0000000000", "1436093.0000000000",
         "22328.0000000000"),
    ])
    def test_get_tmall_conversion_data(self, case, date_start, date_end, status, message, data_date1, paid_amount1,
                                       refunded_amount1,
                                       total_amount1, earning1, data_date2, paid_amount2, refunded_amount2,
                                       total_amount2, earning2, ):
        self.payload = {"date_start": date_start, "date_end": date_end}
        r = requests.get(self.url, headers=self.header, params=self.payload)
        self.result = r.json()
        if date_start == date_end:
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date1)
            self.assertEqual(self.result["data"][0]["paid_amount"], paid_amount1)
            self.assertEqual(self.result["data"][0]["refunded_amount"], refunded_amount1)
            self.assertEqual(self.result["data"][0]["total_amount"], total_amount1)
            self.assertEqual(self.result["data"][0]["earning"], earning1)
        elif case == "日期参数正确(两天)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date1)
            self.assertEqual(self.result["data"][0]["paid_amount"], paid_amount1)
            self.assertEqual(self.result["data"][0]["refunded_amount"], refunded_amount1)
            self.assertEqual(self.result["data"][0]["total_amount"], total_amount1)
            self.assertEqual(self.result["data"][0]["earning"], earning1)
            self.assertEqual(self.result["data"][1]["date"], data_date2)
            self.assertEqual(self.result["data"][1]["paid_amount"], paid_amount2)
            self.assertEqual(self.result["data"][1]["refunded_amount"], refunded_amount2)
            self.assertEqual(self.result["data"][1]["total_amount"], total_amount2)
            self.assertEqual(self.result["data"][1]["earning"], earning2)


if __name__ == "__main__":
    unittest.main()
