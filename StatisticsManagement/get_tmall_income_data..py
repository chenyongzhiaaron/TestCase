import os
import sys
import unittest

import requests

from StatisticsManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetTmallIncomeData(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/income")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    def test_get_tmall_income_data(self):
        self.payload = {"date_start": "2018-04-01", "date_end": "2018-04-01"}
        r = requests.get(self.url, headers=self.header, params=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], 0)
        self.assertEqual(self.result["message"], "success")
        self.assertEqual(self.result["data"][0]["id"], 91)
        self.assertEqual(self.result["data"][0]["date"], "2018-04-01")
        self.assertEqual(self.result["data"][0]["paid_amount"], "41965.0000000000")
        self.assertEqual(self.result["data"][0]["refunded_amount"], "1794.0000000000")
        self.assertEqual(self.result["data"][0]["earning"], "40171.0000000000")
        self.assertEqual(self.result["data"][0]["sales"][0]["id"], 271)
        self.assertEqual(self.result["data"][0]["sales"][0]["record_id"], 91)
        self.assertEqual(self.result["data"][0]["sales"][0]["product_id"], 1)
        self.assertEqual(self.result["data"][0]["sales"][0]["paid_amount"], "1899.0000000000")
        self.assertEqual(self.result["data"][0]["sales"][0]["refunded_amount"], "0.0000000000")
        self.assertEqual(self.result["data"][0]["sales"][0]["earning"], "1899.0000000000")
        self.assertEqual(self.result["data"][0]["sales"][0]["product_name"], "Mars by crazybaby")


if __name__ == '__main__':
    unittest.main()
