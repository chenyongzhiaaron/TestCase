import unittest

import requests
from parameterized import parameterized

from OrderManagement import global_base


class OrderInformation(unittest.TestCase):
    def setUp(self):
        self.url = global_base.Base.url(self, "/order/307")
        self.headers = global_base.Base.headers(self)

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("验证获取订单详情成功", 0, "success", 307, '10201805110316170404', 273, "302721132@qq.com", "asd", "123123", "asdas",
         "asdasd", "asdasd", "United States", "24124", None, "USD", 0, None, 0, 99, 0, "type.normal",
         "order.pending", None)
    ])
    def test_get_order_list(self, case, status, message, id, order_number, user_id, email, recipient, phone_number,
                            address, city, state, country, zip_code, user_note, currency_code, shipping_fee, coupon_id,
                            discount, total_amount, type, type_text, status_text, payment_type):
        self.result = requests.get(self.url, headers=self.headers).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)
        self.assertEqual(self.result["data"]["id"], id)
        self.assertEqual(self.result["data"]["order_number"], order_number)
        self.assertEqual(self.result["data"]["user_id"], user_id)
        self.assertEqual(self.result["data"]["email"], email)
        self.assertEqual(self.result["data"]["recipient"], recipient)
        self.assertEqual(self.result["data"]["phone_number"], phone_number)
        self.assertEqual(self.result["data"]["address"], address)
        self.assertEqual(self.result["data"]["city"], city)
        self.assertEqual(self.result["data"]["state"], state)
        self.assertEqual(self.result["data"]["country"], country)
        self.assertEqual(self.result["data"]["zip_code"], zip_code)
        self.assertEqual(self.result["data"]["user_note"], user_note)
        self.assertEqual(self.result["data"]["currency_code"], currency_code)
        self.assertEqual(self.result["data"]["shipping_fee"], shipping_fee)
        self.assertEqual(self.result["data"]["coupon_id"], coupon_id)
        self.assertEqual(self.result["data"]["discount"], discount)
        self.assertEqual(self.result["data"]["total_amount"], total_amount)
        self.assertEqual(self.result["data"]["type"], type)
        self.assertEqual(self.result["data"]["type_text"], type_text)
        self.assertEqual(self.result["data"]["status_text"], status_text)
        self.assertEqual(self.result["data"]["payment_type"], payment_type)

    @parameterized.expand([
        ("订单号不存在", 400000, "order.invalid")
    ])
    def test_get_order_list_disable(self, case, status, message):
        self.url = global_base.Base.url(self, "/order/3007")
        self.result = requests.get(self.url, headers=self.headers).json()
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)


if __name__ == "__main__":
    unittest.main()
