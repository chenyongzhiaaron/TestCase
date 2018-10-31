import os
import sys
import unittest

import requests
from parameterized import parameterized

from StatisticsManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetTmallEarningDate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/earning")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("天", "2018-04-01", "2018-04-01", 1000, 0, "success", "2018-04-01", 41965, 1794,
         2914.14, 40171, 0.0725433770),
    ])
    def test_get_tmall_earning_date(self, case, date_start, data_end, cycle, status, message, data_data, paid_amount,
                                    refunded_amount,
                                    ad_rate, earning, acost):
        payload = {"date_start": date_start, "date_end": data_end, "cycle": cycle}
        r = requests.get(self.url, headers=self.header, params=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"][0]["date"], data_data)
        self.assertEqual(self.result["data"][0]["paid_amount"], paid_amount)
        self.assertEqual(self.result["data"][0]["refunded_amount"], refunded_amount)
        self.assertEqual(self.result["data"][0]["ad_rate"], ad_rate)
        self.assertEqual(self.result["data"][0]["earning"], earning)
        self.assertEqual(self.result["data"][0]["acost"], acost)


if __name__ == "__main__":
    unittest.main()