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
        self.url = global_base.Base.url(self, "/browse")
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("日期参数正确(当前天)", "2018-04-01", "2018-04-01", 0, "success", "2018-04-01", 6845, 19249, "", "", ""),
        ("日期参数正确(两天)", "2018-04-01", "2018-04-02", 0, "success", "2018-04-01", 6845, 19249,  "2018-04-02", 4846, 14259),
    ])
    def test_get_tmall_browse_data(self, case, date_start, date_end, status, message, data_date1, visitor1, page_view1, data_date2, visitor2, page_view2):
        self.payload = {"date_start": date_start, "date_end": date_end}
        r = requests.get(self.url, headers=self.header, params=self.payload)
        self.result = r.json()
        if date_start == date_end:
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date1)
            self.assertEqual(self.result["data"][0]["visitor"], visitor1)
            self.assertEqual(self.result["data"][0]["page_view"], page_view1)
        elif case == "日期参数正确(两天)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date1)
            self.assertEqual(self.result["data"][0]["visitor"], visitor1)
            self.assertEqual(self.result["data"][0]["page_view"], page_view1)
            self.assertEqual(self.result["data"][1]["date"], data_date2)
            self.assertEqual(self.result["data"][1]["visitor"], visitor2)
            self.assertEqual(self.result["data"][1]["page_view"], page_view2)


if __name__ == "__main__":
    unittest.main()
