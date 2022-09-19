import unittest
from utils.request import req 

class TestCreateAccount(unittest.TestCase):

    def test_create_fail(self):
        payloads = {
            "user_id":1,
            "bank":"TTB",
            "amount":100,
            "channel":"Android"
        }
        res = req("http://localhost:8000/api/open_account", payloads)
        self.assertNotEqual(res.status_code,200)
    
    def test_create_pass1(self):
        payloads = {
            "user_id":1,
            "bank":"TTB",
            "amount":500,
            "channel":"Android"
        }
        res = req("http://localhost:8000/api/open_account", payloads)
        self.assertEqual(res.status_code,200)

    def test_create_pass2(self):
        payloads = {
            "user_id":1,
            "bank":"TTB",
            "amount":1000,
            "channel":"Android"
        }
        res = req("http://localhost:8000/api/open_account", payloads)
        self.assertEqual(res.status_code,200)

if __name__ == '__main__':
    unittest.main()