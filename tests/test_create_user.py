import unittest
from utils.request import req 
from utils.find_user import find_user

class TestCreateUser(unittest.TestCase):

    def test_create(self):
        payloads = {
            "name": "John Doe"
        }
        res = req("http://localhost:8000/api/create_user", payloads)
        self.assertEqual(res.status_code,200)
    
    def test_exists(self):
        self.assertIsNotNone(find_user('John Doe'))

if __name__ == '__main__':
    unittest.main()