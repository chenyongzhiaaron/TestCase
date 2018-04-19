import unittest
import requests
from ProductManagement import global_base
from parameterized import parameterized
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class UpdateProductSuccess(unittest.TestCase):

    def setUp(self):
        self.urlDraft = global_base.BaseUrl.url(self, "/products/774/note")
        self.urlReleased = global_base.BaseUrl.url(self, "/products/765/note")
        self.urlDisabel = global_base.BaseUrl.url(self, "/products/738/note")
        self.headers = global_base.BaseUrl.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("id_draft", 1234567890, 0, "success", 774, "1234567890")
    ])
    def test_update_draftProduct_success(self, case, note, status, message, data_id, data_note):
        self.payload = {"note": note}
        r = requests.patch(self.urlDraft, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["note"], data_note)

    @parameterized.expand([
        ("id_released", "abcABC", 0, "success", 765, "abcABC",)
    ])
    def test_update_draftProduct_success(self, case, note, status, message, data_id, data_note):
        self.payload = {"note": note}
        r = requests.patch(self.urlReleased, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["note"], data_note)

    @parameterized.expand([
        ("id_disable", "/\\\&?/\\/", 0, "success", 738, "/\\\&?/\\/")
    ])
    def test_update_draftProduct_success(self, case, note, status, message, data_id, data_note):
        self.payload = {"note": note}
        r = requests.patch(self.urlDisabel, headers=self.headers, data=self.payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], data_id)
        self.assertEqual(self.result["data"]["note"], data_note)

if __name__ == "__main__":
    unittest.main()