import unittest
import requests
import os
import sys
from ProductManagement import global_base

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)


class DelectdeProduct(unittest.TestCase):

    def setUp(self):
        self.urlIdNull = global_base.Base.url(self, "/products/{id}")
        self.urlIdInvalid = global_base.Base.url(self, "/products/89893")
        self.urlIdReleased = global_base.Base.url(self, "/products/767")
        self.header = global_base.Base.headers