import os
import sys
import unittest

import requests
from parameterized import parameterized

from StatisticsManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetTmallConversionDate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/conversion")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("日期参数正确(当前天)", "2018-04-01", "2018-04-01", 0, "success", "2018-04-01", 6845, "41965.0000000000", "0.0093000000",
         "0.93%", "", "", "", "", ""),
        ("日期参数正确(两天)", "2018-04-01", "2018-04-02", 0, "success", "2018-04-01", 6845, "41965.0000000000", "0.0093000000",
         "0.93%", "2018-04-02", 4846, "23524.0000000000", "0.0074000000", "0.74%"),
    ])
    def test_get_tmall_conversion_data(self, case, date_start, date_end, status, message, data_date1, visitor1,
                                       paid_amount1,
                                       conversion_ratio1, conversion_rate1, data_date2, visitor2, paid_amount2,
                                       conversion_ratio2, conversion_rate2, ):
        self.payload = {"date_start": date_start, "date_end": date_end}
        r = requests.get(self.url, headers=self.header, params=self.payload)
        self.result = r.json()
        if date_start == date_end:
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date1)
            self.assertEqual(self.result["data"][0]["visitor"], visitor1)
            self.assertEqual(self.result["data"][0]["paid_amount"], paid_amount1)
            self.assertEqual(self.result["data"][0]["conversion_ratio"], conversion_ratio1)
            self.assertEqual(self.result["data"][0]["conversion_rate"], conversion_rate1)
        elif case == "日期参数正确(两天)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date1)
            self.assertEqual(self.result["data"][0]["visitor"], visitor1)
            self.assertEqual(self.result["data"][0]["paid_amount"], paid_amount1)
            self.assertEqual(self.result["data"][0]["conversion_ratio"], conversion_ratio1)
            self.assertEqual(self.result["data"][0]["conversion_rate"], conversion_rate1)
            self.assertEqual(self.result["data"][1]["date"], data_date2)
            self.assertEqual(self.result["data"][1]["visitor"], visitor2)
            self.assertEqual(self.result["data"][1]["paid_amount"], paid_amount2)
            self.assertEqual(self.result["data"][1]["conversion_ratio"], conversion_ratio2)
            self.assertEqual(self.result["data"][1]["conversion_rate"], conversion_rate2)


if __name__ == "__main__":
    unittest.main()
