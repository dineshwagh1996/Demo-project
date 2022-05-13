import unittest
from unittest.mock import MagicMock

class testdemo(unittest.TestCase):

    def setUp(self):
        from src import demo_lambda
        self.demo_lambda=demo_lambda


    def test_lambda(self):
        event={'first_name':'rohit','last_name':'patil'}
        key='Test'
        container="Test Result"
        result=self.demo_lambda.lambda_handler(event,MagicMock())
        self.assertIn(key,container,result)

    def tearDown(self):
        print("tear down method...")


if __name__ == '__main__':
    unittest.main()



