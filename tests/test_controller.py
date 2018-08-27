import unittest
import json

from app import create_app


class ControllerTestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app({
            'TESTING': True
        })
        self.client = self.app.test_client()

    def test_get_health_ok(self):
        response = self.client.get('/health') 
        self.assertEqual(response.status_code, 200)

    def test_get_patients_autocomplete_ok(self):
        response = self.client.get('/patients/autocomplete?q=abby%20ba')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
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
        self.assertEqual(data['records'][0]['name'], 'abby bates')

    def test_get_patients_autocomplete_without_queryparam_q(self):
        response = self.client.get('/patients/autocomplete?')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(type(data), dict)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'query param q is required')
        self.assertIn('errorCode', data)
        self.assertEqual(data['errorCode'], '40000')

    def test_get_patients_autocomplete_without_queryparam_q(self):
        response = self.client.get('/patients/autocomplete?q=')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(type(data), dict)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'query param q is required')
        self.assertIn('errorCode', data)
        self.assertEqual(data['errorCode'], '40000')

    def test_get_patients_autocomplete_queryparam_q_min_length(self):
        response = self.client.get('/patients/autocomplete?q=a')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(type(data), dict)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'min of two characters')
        self.assertIn('errorCode', data)
        self.assertEqual(data['errorCode'], '40001')

    def test_get_patients_autocomplete_not_found(self):
        response = self.client.get('/patients/autocomplete?q=notfound')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertEqual(type(data), dict)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'patient not found')
        self.assertIn('errorCode', data)
        self.assertEqual(data['errorCode'], '40400')


if __name__ == '__main__':
    unittest.main()