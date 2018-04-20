import os
import sys
import unittest

import requests
from parameterized import parameterized

from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)


class DeletedProduct(unittest.TestCase):
    def setUp(self):
        self.urlIdNull = global_base.Base.url(self, "/products/{id}/packs")  # 不合法 id
        self.urlIdInvalid = global_base.Base.url(self, "/products/89893/packs")  # id 89893 不存在数据库
        self.urlIdReleased = global_base.Base.url(self, "/products/739/packs")  # id 739 已上架
        self.urlIdDisable = global_base.Base.url(self, "/products/588/packs")  # id 588 已下架
        self.urlIdDraft = global_base.Base.url(self, "/products/781/packs")  # id 781 草稿
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("验证ID不合法，请求失败", 404000, "request.not.found"),
    ])
    def test_store_prodcut_pack_null(self, case, status, message):
        r = requests.post(self.urlIdNull, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("验证ID不存在数据库，修改失败", 422000, "illegal.request.data", ['required']),
    ])
    def test_store_product_pack_invalid(self, case, status, message, error):
        r = requests.post(self.urlIdInvalid, headers=self.header)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["error"]["packs"], error)

    @parameterized.expand([
        ("验证ID已上架，修改失败", 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 400000, "product.invalid"),
    ])
    def test_store_product_pack_release(self, case, units, net_weight, rough_weight, height, width, length, status,
                                        message):
        self.payload = {"packs[0][units]": units, "packs[0][net_weight]": net_weight,
                        "packs[0][rough_weight]": rough_weight, "packs[0][height]": height, "packs[0][width]": width,
                        "packs[0][length]": length}
        r = requests.post(self.urlIdInvalid, headers=self.header, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

    @parameterized.expand([
        ("验证ID已下架，修改成功，所有值最小", 0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0, "success", "0.0010000000", "0.0010000000",
         "0.0020000000", '0.0010000000', '0.0010000000', '0.0010000000', '0.001', '0.001', '0.002', "0.001", "0.001",
         "0.001"),
    ])
    def test_store_product_pack_disable(self, case, units, net_weight, rough_weight, height, width, length, status,
                                        message, data_units, data_net_weight, data_rough_weight, data_height,
                                        data_width, data_length, units_text, net_weight_text, rough_weight_text,
                                        height_text, width_text, length_text):
        self.payload = {"packs[0][units]": units, "packs[0][net_weight]": net_weight,
                        "packs[0][rough_weight]": rough_weight, "packs[0][height]": height, "packs[0][width]": width,
                        "packs[0][length]": length}
        r = requests.post(self.urlIdDisable, headers=self.header, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"][0]["units"], data_units)
        self.assertEqual(self.result["data"][0]["net_weight"], data_net_weight)
        self.assertEqual(self.result["data"][0]["rough_weight"], data_rough_weight)
        self.assertEqual(self.result["data"][0]["height"], data_height)
        self.assertEqual(self.result["data"][0]["width"], data_width)
        self.assertEqual(self.result["data"][0]["length"], data_length)
        self.assertEqual(self.result["data"][0]["units_text"], units_text)
        self.assertEqual(self.result["data"][0]["net_weight_text"], net_weight_text)
        self.assertEqual(self.result["data"][0]["rough_weight_text"], rough_weight_text)
        self.assertEqual(self.result["data"][0]["height_text"], height_text)
        self.assertEqual(self.result["data"][0]["width_text"], width_text)
        self.assertEqual(self.result["data"][0]["length_text"], length_text)

    @parameterized.expand([
        ("max", 99999999, 99999998, 99999999, 99999999, 99999999, 99999999, 0, "success",
         "99999999.0000000000", "99999998.0000000000",
         "99999999.0000000000", "99999999.0000000000", "99999999.0000000000", "99999999.0000000000", "99,999,999",
         "99,999,998", "99,999,999", "99,999,999", "99,999,999",
         "99,999,999"),
        ("max-1", 99999998, 99999997, 99999998, 99999998, 99999998, 99999998, 0, "success",
         "99999998.0000000000", "99999997.0000000000",
         "99999998.0000000000", "99999998.0000000000", "99999998.0000000000", "99999998.0000000000", "99,999,998",
         "99,999,997", "99,999,998", "99,999,998", "99,999,998",
         "99,999,998"),
    ])
    def test_store_product_pack_draft(self, case, units, net_weight, rough_weight, height, width, length, status,
                                      message, data_units, data_net_weight, data_rough_weight, data_height,
                                      data_width, data_length, units_text, net_weight_text, rough_weight_text,
                                      height_text, width_text, length_text):
        self.payload = {"packs[0][units]": units, "packs[0][net_weight]": net_weight,
                        "packs[0][rough_weight]": rough_weight, "packs[0][height]": height, "packs[0][width]": width,
                        "packs[0][length]": length}
        r = requests.post(self.urlIdDraft, headers=self.header, data=self.payload)
        if units == 99999999:
            self.result = r.json()
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][0]["units"], data_units)
            self.assertEqual(self.result["data"][0]["net_weight"], data_net_weight)
            self.assertEqual(self.result["data"][0]["rough_weight"], data_rough_weight)
            self.assertEqual(self.result["data"][0]["height"], data_height)
            self.assertEqual(self.result["data"][0]["width"], data_width)
            self.assertEqual(self.result["data"][0]["length"], data_length)
            self.assertEqual(self.result["data"][0]["units_text"], units_text)
            self.assertEqual(self.result["data"][0]["net_weight_text"], net_weight_text)
            self.assertEqual(self.result["data"][0]["rough_weight_text"], rough_weight_text)
            self.assertEqual(self.result["data"][0]["height_text"], height_text)
            self.assertEqual(self.result["data"][0]["width_text"], width_text)
            self.assertEqual(self.result["data"][0]["length_text"], length_text)
        elif net_weight == 99999997:
            self.result = r.json()
            self.assertEqual(self.result["status"], status)
            self.assertEqual(self.result["message"], message)
            self.assertEqual(self.result["data"][1]["units"], data_units)
            self.assertEqual(self.result["data"][1]["net_weight"], data_net_weight)
            self.assertEqual(self.result["data"][1]["rough_weight"], data_rough_weight)
            self.assertEqual(self.result["data"][1]["height"], data_height)
            self.assertEqual(self.result["data"][1]["width"], data_width)
            self.assertEqual(self.result["data"][1]["length"], data_length)
            self.assertEqual(self.result["data"][1]["units_text"], units_text)
            self.assertEqual(self.result["data"][1]["net_weight_text"], net_weight_text)
            self.assertEqual(self.result["data"][1]["rough_weight_text"], rough_weight_text)
            self.assertEqual(self.result["data"][1]["height_text"], height_text)
            self.assertEqual(self.result["data"][1]["width_text"], width_text)
            self.assertEqual(self.result["data"][1]["length_text"], length_text)



if __name__ == "__main__":
    unittest.main()
