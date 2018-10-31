class Base():
    def url(self, patch):
        baseurl = 'http://api.cosmos.crazybaby.com/api/omm/v1'
        self.url = baseurl + patch
        return self.url

    def headers(self):
        self.headers = {
            'accept': "application/json",
            'secret': "oFCPQTbo1t4KcMvys05wKLXhCTujhgvz",
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjk3LCJpc3MiOi"
                             "JodHRwOi8vYXBpLmNvc21vcy5jcmF6eWJhYnkuY29tL2FwaS92MS9hY2Nlc3MvdG"
                             "9rZW4iLCJpYXQiOjE1MjU4NTYxNzEsImV4cCI6MTUyODQ0ODE3MSwibmJmIjoxNTI1ODU2MTcxLCJ"
                             "qdGkiOiJBZmwxT1hpN1NnZXcxVkFsIn0.AW5L0hloq9tsYzJhigdbtX7-IpKGGsXFQW4hoqU3AJg"
        }
        return self.headers
