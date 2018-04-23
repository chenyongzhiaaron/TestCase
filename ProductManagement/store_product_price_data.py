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
        self.urlIdNull = global_base.Base.url(self, "/products/{id}/prices")  # 不合法 id
        self.urlIdInvalid = global_base.Base.url(self, "/products/89893/prices")  # id 89893 不存在数据库
        self.urlIdReleased = global_base.Base.url(self, "/products/739/prices")  # id 739 已上架
        self.urlIdDisable = global_base.Base.url(self, "/products/588/prices")  # id 588 已下架
        self.urlIdDraft = global_base.Base.url(self, "/products/781/prices")  # id 781 草稿
        self.header = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    # @parameterized.expand([
    #     ("验证ID不合法，请求失败", 404000, "request.not.found"),
    # ])
    # def test_delected_product_null(self, case, status, message):
    #     r = requests.post(self.urlIdNull, headers=self.header)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], status)
    #     self.assertEqual(self.result["message"], message)
    #
    # @parameterized.expand([
    #     ("验证ID不存在数据库，修改失败", 422000, "illegal.request.data", ["required"]),
    # ])
    # def test_delected_product_invalid(self, case, status, message, error_prices):
    #     r = requests.post(self.urlIdInvalid, headers=self.header)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], status)
    #     self.assertEqual(self.result["message"], message)
    #     self.assertEqual(self.result["error"]["prices"], error_prices)

    # @parameterized.expand([
    #     ("验证ID以释放，修改价格失败", "CN", "CNY", 1999, "fault错误", "白色", 400000, "product.invalid"),
    # ])
    # def test_delected_product_released(self, case, country, currency, price, name, color, status, message):
    #     self.payload = {"prices[0][country_code]": country, "prices[0][currency_code]": currency,
    #                     "prices[0][price]": price, "prices[0][name]": name, "prices[0][color]": color}
    #     r = requests.post(self.urlIdReleased, headers=self.header, data=self.payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], status)
    #     self.assertEqual(self.result["message"], message)

    # @parameterized.expand([
    #     ("验证ID已下架，修改价格成功", "CN", "CNY", 1999, "价格名称", "价格颜色白色", 0, "success", "CN", "CNY", '1999.0000000000', "价格名称",
    #      "价格颜色白色",
    #      "1,999"),
    # ])
    # def test_delected_product_released(self, case, country, currency, price, name, color, status, message,
    #                                    data_country, data_currency, data_price, data_name, data_color, data_price_text):
    #     self.payload = {"prices[0][country_code]": country, "prices[0][currency_code]": currency,
    #                     "prices[0][price]": price, "prices[0][name]": name, "prices[0][color]": color}
    #     r = requests.post(self.urlIdDisable, headers=self.header, data=self.payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], status)
    #     self.assertEqual(self.result["message"], message)
    #     self.assertEqual(self.result["data"][0]["country_code"], data_country)
    #     self.assertEqual(self.result["data"][0]["currency_code"], data_currency)
    #     self.assertEqual(self.result["data"][0]["price"], data_price)
    #     self.assertEqual(self.result["data"][0]["name"], data_name)
    #     self.assertEqual(self.result["data"][0]["color"], data_color)
    #     self.assertEqual(self.result["data"][0]["price_text"], data_price_text)
    #
    # @parameterized.expand([
    #     ("验证ID草稿，修改价格成功", "CN", "CNY", 1999, "价格名称", "价格颜色白色", 0, "success", "CN", "CNY", '1999.0000000000', "价格名称",
    #      "价格颜色白色",
    #      "1,999"),
    # ])
    # def test_delected_product_released(self, case, country, currency, price, name, color, status, message,
    #                                    data_country, data_currency, data_price, data_name, data_color, data_price_text):
    #     self.payload = {"prices[0][country_code]": country, "prices[0][currency_code]": currency,
    #                     "prices[0][price]": price, "prices[0][name]": name, "prices[0][color]": color}
    #     r = requests.post(self.urlIdDraft, headers=self.header, data=self.payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], status)
    #     self.assertEqual(self.result["message"], message)
    #     self.assertEqual(self.result["data"][0]["country_code"], data_country)
    #     self.assertEqual(self.result["data"][0]["currency_code"], data_currency)
    #     self.assertEqual(self.result["data"][0]["price"], data_price)
    #     self.assertEqual(self.result["data"][0]["name"], data_name)
    #     self.assertEqual(self.result["data"][0]["color"], data_color)
    #     self.assertEqual(self.result["data"][0]["price_text"], data_price_text)

    @parameterized.expand([
        ("验证country_code最大值", "123", "CNY", 1999, "价格名称", "价格颜色白色", 0, "success", "123", "CNY", '1999.0000000000',
         "价格名称",
         "价格颜色白色",
         "1,999"),

    ])
    def test_delected_product_released(self, case, country, currency, price, name, color, status, message,
                                       data_country, data_currency, data_price, data_name, data_color, data_price_text):
        self.payload = {"prices[0][country_code]": country, "prices[0][currency_code]": currency,
                        "prices[0][price]": price, "prices[0][name]": name, "prices[0][color]": color}
        r = requests.post(self.urlIdDraft, headers=self.header, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"][0]["country_code"], data_country)
        self.assertEqual(self.result["data"][0]["currency_code"], data_currency)
        self.assertEqual(self.result["data"][0]["price"], data_price)
        self.assertEqual(self.result["data"][0]["name"], data_name)
        self.assertEqual(self.result["data"][0]["color"], data_color)
        self.assertEqual(self.result["data"][0]["price_text"], data_price_text)


if __name__ == "__main__":
    unittest.main()
