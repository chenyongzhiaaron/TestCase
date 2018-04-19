import unittest
import requests
from ProductManagement import global_base
from parameterized import parameterized
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class StoreProductDataSuccess(unittest.TestCase):

    def setUp(self):
        self.url = global_base.BaseUrl.url(self, "/products")
        self.headers = global_base.BaseUrl.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("color1000_type0_success", 0, "Test_interface_product10", "Test_product", 1000, " ", "Test", 0, "success", 0, "Test_interface_productA123", "Test_product", 1000, None, "Test", 0),
        ("color2000_type0_success", 0, "汉字", "Test_product", 1000, " ", "descirption", 0, "success", 0, "Test_interface_productA123", "Test_product", 2000, None, "Test", 0),
        ("color3000_type0_success", 0, "[]", "Test_product", 1000, " ", "DESCRIPTION", 0, "success", 0, "Test_interface_productA123", "Test_product", 3000, None, "Test", 0),
        ("color4000_type0_success", 0, "", "Test_product", 1000, " ", "汉字", 0, "success", 0, "Test_interface_productA123", "Test_product", 4000, None, "Test", 0),
        ("color5000_type0_success", 0, "Test_interface_product14", "Test_product", 1000, " ", "｛｝", 0, "success", 0, "Test_interface_productA123", "Test_product", 5000, None, "Test", 0),
        ("color6000_type0_success", 0, "Test_interface_product15", "Test_product", 1000, " ", "{}", 0, "success", 0, "Test_interface_productA123", "Test_product", 6000, None, "Test", 0),
        ("color7000_type0_success", 0, "Test_interface_product16", "Test_product", 1000, " ", ".//*[@id='preview']/ul[7]/li", 0, "success", 0, "Test_interface_productA123", "Test_product", 7000, None, "Test", 0),
        ("color8000_type0_success", 0, "Test_interface_product17", "Test_product", 1000, " ", "1", 0, "success", 0, "Test_interface_productA123", "Test_product", 8000, None, "Test", 0),
        ("color9000_type0_success", 0, "Test_interface_product18", "Test_product", 1000, " ", "12", 0, "success", 0, "Test_interface_productA123", "Test_product", 9000, None, "Test", 0),
        ("color10000_type0_success", 0, "Test_interface_product19", "Test_product", 1000, " ", "", 0, "success", 0, "Test_interface_productA123", "Test_product", 10000, None, "Test", 0),
        ("color11000_type0_success", 0, "Test_interface_product20", "Test_product", 1000, " ", "Test", 0, "success", 0, "Test_interface_productA123", "Test_product", 11000, None, "Test", 0),
        ("color12000_type0_success", 0, "Test_interface_product21", "Test_product", 1000, " ", "Test", 0, "success", 0, "Test_interface_productA123", "Test_product", 12000, None, "Test", 0),
        ("color13000_type0_success", 0, "Test_interface_product22", "Test_product", 1000, " ", "Test", 0, "success", 0, "Test_interface_productA123", "Test_product", 13000, None, "Test", 0),
        ("color14000_type0_success", 0, "Test_interface_product23", "Test_product", 1000, " ", "Test", 0, "success", 0, "Test_interface_productA123", "Test_product", 14000, None, "Test", 0),
        # ("product_create_color2000_type0_success", 0, "Test_interface_product11", "Test_product", 2000, "1", "汉字", 0, "success", 0, "Test_interface_product11", "Test_product", 2000, ),
        # ("product_create_color3000_type0_success", 0, "Test_interface_product12", "Test_product", 3000, "abc", "abc", 0, "success", 0, "Test_interface_product12", "Test_product", 3000),
        # ("product_create_color4000_type0_success", 0, "Test_interface_product13", "Test_product", 4000, "汉字", "12345", 0, "success", 0, "Test_interface_product13", "Test_product", 4000),
        # ("product_create_color5000_type0_success", 0, "Test_interface_product14", "Test_product", 5000, "｛｝", "{[]}", 0, "success",0, "Test_interface_product14", "Test_product", 5000),
        # ("product_create_color6000_type0_success", 0, "Test_interface_product15", "Test_product", 6000, "。。。", "ABC", 0, "success", 0, "Test_interface_product15", "Test_product", 6000),
        # ("product_create_color7000_type0_success", 0, "Test_interface_product16", "Test_product", 7000, "ABC", "null", 0, "success", 0, "Test_interface_product16", "Test_product", 7000),
        # ("product_create_color8000_type0_success", 0, "Test_interface_product17", "Test_product", 8000, "12径.a&C", "Test", 0, "success", 0, "Test_interface_product17", "Test_product", 8000,),
    ])
    def test_store_product_data_success(self, case_name, type, name, model, color, hs_code, description, status, message, result__data_type, result_data_name, result_data_model, result_data_color,
                                        result_data_hs_code, result_data_description, result_data_status):
        self.payload = {"type": type, "name": name, "model": model, "color": color, "hs_code": hs_code, "description": description}
        r = requests.post(self.url, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["type"], result__data_type)
        self.assertEqual(self.result["data"]["name"], result_data_name)
        self.assertEqual(self.result["data"]["model"], result_data_model)
        self.assertEqual(self.result["data"]["color"], result_data_color)
        self.assertEqual(self.result["data"]["hs_code"], result_data_hs_code)
        self.assertEqual(self.result["data"]["description"], result_data_description)
        self.assertEqual(self.result["data"]["status"], result_data_status)

if __name__ == "__main__":
    unittest.main()