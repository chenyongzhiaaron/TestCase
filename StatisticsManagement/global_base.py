class Base():
    def url(self, patch):
        base = 'http://api.cosmos.crazybaby.com/api/stm/v1/tmall'
        self.url = base + patch
        return self.url

    def headers(self):
        headers = {
            'accept': "application/json",
            'secret': "oFCPQTbo1t4KcMvys05wKLXhCTujhgvz",
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1N"
                             "iJ9.eyJzdWIiOjk3LCJpc3MiOiJodHRwOi8vYXBpLmNvc21vcy5jcm"
                             "F6eWJhYnkuY29tL2FwaS92MS9hY2Nlc3MvdG9rZW4iLCJpYXQiOjE1MjM1MDM4NjAsImV4cCI6MTUyN"
                             "jA5NTg2MCwibmJmIjoxNTIzNTAzODYwLCJqdGkiOiJ6RXNZODZHbjhQMTdDMmo1"
                             "In0.QhSfvDHJ2im_jj09tQQdq8THXXOFnaaN5X_gZIRhkIA"
        }

        return headers
