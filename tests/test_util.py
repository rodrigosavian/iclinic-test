import os
import unittest
import json

from http import HTTPStatus

from app import create_app, util


class UtilTestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app({
            'TESTING': True
        })

    def test_csv_reader_ok(self):
        result = util.csv_reader(os.path.join(self.app.config['PROJECT_PATH'], 'patients.csv'))
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 4147)

    def test_response_success_ok(self):
        response = util.response_success([{'name': 'mark'}], HTTPStatus.OK)
        self.assertEqual(type(response), tuple)
        self.assertEqual(len(response), 3)
        self.assertEqual(type(response[0]), str)
        data = json.loads(response[0])
        self.assertEqual(type(data), dict)
        self.assertIn('meta', data)
        self.assertEqual(type(data['meta']), dict)
        self.assertIn('version', data['meta'])
        self.assertEqual(data['meta']['version'], 'v1.0.0')
        self.assertIn('records', data)
        self.assertEqual(type(data['records']), list)
        self.assertEqual(len(data['records']), 1)
        self.assertEqual(type(data['records'][0]), dict)
        self.assertIn('name', data['records'][0])
        self.assertEqual(data['records'][0]['name'], 'mark')
        self.assertTrue(isinstance(response[1], int))
        self.assertEqual(type(response[2]), dict)

    def test_response_error_ok(self):
        response = util.response_error(('message', 'error_code'), HTTPStatus.BAD_REQUEST)
        self.assertEqual(type(response), tuple)
        self.assertEqual(len(response), 3)
        self.assertEqual(type(response[0]), str)
        data = json.loads(response[0])
        self.assertEqual(type(data), dict)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'message')
        self.assertIn('errorCode', data)
        self.assertEqual(data['errorCode'], 'error_code')
        self.assertTrue(isinstance(response[1], int))
        self.assertEqual(type(response[2]), dict)


if __name__ == '__main__':
    unittest.main()