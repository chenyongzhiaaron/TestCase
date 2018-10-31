class Base():
    def url(self, patch):
        base = 'http://api.cosmos.crazybaby.com/api/stm/v1/tmall'
        self.url = base + patch
        return self.url

    def headers(self):
        headers = {
            'accept': "application/json",
            'secret': "oFCPQTbo1t4KcMvys05wKLXhCTujhgvz",
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjk3LCJpc3MiOiJodHRwOi8vYXBpLmNvc21vcy5jcmF6eWJhYnkuY29tL2FwaS92MS9hY2Nlc3MvdG9rZW4iLCJpYXQiOjE1MjU4NTYxNzEsImV4cCI6MTUyODQ0ODE3MSwibmJmIjoxNTI1ODU2MTcxLCJqdGkiOiJBZmwxT1hpN1NnZXcxVkFsIn0.AW5L0hloq9tsYzJhigdbtX7-IpKGGsXFQW4hoqU3AJg"
        }

        return headers
