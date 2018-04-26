import os
import sys
import unittest
import requests
from parameterized import parameterized
from StatisticsManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class GetTmallEstimateDate(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/estimate")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("输入正确的日期获取数据成功", "2018-04-01", "2018-04-01", 0, "success", "2018-04-01", "4.7496600000", "4.8012600000",
         "4.7954200000", 0, 0),
    ])
    def test_get_tmall_estimate_date(self, case, date_start, data_end, status, message, data_data, description_rating,
                                     service_rating,
                                     logistics_rating, favourable_comment, negative_comment):
        payload = {"date_start": date_start, "date_end": data_end}
        r = requests.get(self.url, headers=self.header, params=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"][0]["date"], data_data)
        self.assertEqual(self.result["data"][0]["description_rating"], description_rating)
        self.assertEqual(self.result["data"][0]["service_rating"], service_rating)
        self.assertEqual(self.result["data"][0]["logistics_rating"], logistics_rating)
        self.assertEqual(self.result["data"][0]["favourable_comment"], favourable_comment)
        self.assertEqual(self.result["data"][0]["negative_comment"], negative_comment)


if __name__ == "__main__":
    unittest.main()
