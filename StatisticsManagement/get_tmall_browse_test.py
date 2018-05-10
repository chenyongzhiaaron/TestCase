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
        ("日期参数正确(当前天)", "2018-04-01", "2018-04-01", 1000, 0, "success", "2018-04-01", 6845, 19249, "", "", ""),
        ("日期参数正确(两天)", "2018-04-01", "2018-04-02", 1000, 0, "success", "2018-04-01", 6845, 19249, "2018-04-02", 4846, 14259),
        ("日期参数正确(10天)", "2018-04-01", "2018-04-11", 2000, 0, "success", "2018M4W1", 23744, 78381, "2018M4W2", 8817, 36461),
        ("日期参数正确(1季度)", "2018-01-01", "2018-04-02", 4000, 0, "success", "2018Q1", 389364, 1422255, "2018Q2", 11691, 33508),
        ("日期参数正确(1年)", "2017-01-01", "2018-04-02", 5000, 0, "success", "Y2017", 447709, 1651958, "Y2018", 401055, 1455763),
    ])
    def test_get_tmall_browse_data(self, case, date_start, date_end, cycle, status, message, data_date, visitor,
                                   page_view, date_date2, visitor2, page_view2):
        self.payload = {"date_start": date_start, "date_end": date_end, "cycle": cycle}
        r = requests.get(self.url, headers=self.header, params=self.payload)
        self.result = r.json()
        if date_start == date_end:
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date)
            self.assertEqual(self.result["data"][0]["visitor"], visitor)
            self.assertEqual(self.result["data"][0]["page_view"], page_view)
        elif case == "日期参数正确(两天)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date)
            self.assertEqual(self.result["data"][0]["visitor"], visitor)
            self.assertEqual(self.result["data"][0]["page_view"], page_view)
            self.assertEqual(self.result["data"][1]["date"], date_date2)
            self.assertEqual(self.result["data"][1]["visitor"], visitor2)
            self.assertEqual(self.result["data"][1]["page_view"], page_view2)
        elif case == "日期参数正确(10天)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date)
            self.assertEqual(self.result["data"][0]["visitor"], visitor)
            self.assertEqual(self.result["data"][0]["page_view"], page_view)
            self.assertEqual(self.result["data"][1]["date"], date_date2)
            self.assertEqual(self.result["data"][1]["visitor"], visitor2)
            self.assertEqual(self.result["data"][1]["page_view"], page_view2)
        elif case == "日期参数正确(1季度)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date)
            self.assertEqual(self.result["data"][0]["visitor"], visitor)
            self.assertEqual(self.result["data"][0]["page_view"], page_view)
        elif case == "日期参数正确(1年)":
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["date"], data_date)
            self.assertEqual(self.result["data"][0]["visitor"], visitor)
            self.assertEqual(self.result["data"][0]["page_view"], page_view)


if __name__ == "__main__":
    unittest.main()
