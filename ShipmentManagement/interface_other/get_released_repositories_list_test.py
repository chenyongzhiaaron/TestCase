import unittest
import requests
import os, sys
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parentdir)
from db_fixture import test_data


class GetReleasedRepositoriesList(unittest.TestCase):
    ''' 获取释放仓库列表 '''

    def setUp(self):
        self.base_url = "http://api.cosmos.crazybaby.com/api/smm/v1/repositories"
        self.payload = {
            'accept': "application/json",
            'secret': "oFCPQTbo1t4KcMvys05wKLXhCTujhgvz",
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjk3LCJpc3MiOiJodHRwOi8"
                             "vYXBpLmNvc21vcy5jcmF6eWJhYnkuY29tL2FwaS92MS9hY2Nlc3MvdG9rZW4iLCJpYXQiOjE1MjA5MDgwMzgsIm"
                             "V4cCI6MTUyMzUwMDAzOCwibmJmIjoxNTIwOTA4MDM4LCJqdGkiOiJIQms4b0pVU3NqNUpRQUZOIn0.dPUKe_YVzIECZWROZvqiaa7Kvuu1isGb9QgDsxRHYEA",
        }

    def tearDown(self):
        print(self.result)

    def test_get_repository_products_list(self):
        ''' 所有参数为空 '''
        r = requests.get(self.base_url, headers=self.payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['message'], 'success')


if __name__ == '__main__':
    # test_data.init_data() # 初始化接口测试数据
    unittest.main()
