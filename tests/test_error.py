import unittest

from app.patients import error


class ErrorTestClass(unittest.TestCase):

    def test_err_patients_autocomplete_queryparam_q_required_ok(self):
        err = getattr(error, 'ERR_PATIENTS_AUTOCOMPLETE_QUERYPARAM_Q_REQUIRED')
        self.assertEqual(type(err), tuple)
        self.assertEqual(len(err), 2)
        self.assertEqual(type(err[0]), str)
        self.assertEqual(err[0], 'query param q is required')
        self.assertEqual(type(err[1]), str)
        self.assertEqual(err[1], '40000')

    def test_err_patients_autocomplete_queryparam_q_min_length_ok(self):
        err = getattr(error, 'ERR_PATIENTS_AUTOCOMPLETE_QUERYPARAM_Q_MIN_LENGTH')
        self.assertEqual(type(err), tuple)
        self.assertEqual(len(err), 2)
        self.assertEqual(type(err[0]), str)
        self.assertEqual(err[0], 'min of two characters')
        self.assertEqual(type(err[1]), str)
        self.assertEqual(err[1], '40001')

    def test_err_patients_autocomplete_not_found_ok(self):
        err = getattr(error, 'ERR_PATIENTS_AUTOCOMPLETE_NOT_FOUND')
        self.assertEqual(type(err), tuple)
        self.assertEqual(len(err), 2)
        self.assertEqual(type(err[0]), str)
        self.assertEqual(err[0], 'patient not found')
        self.assertEqual(type(err[1]), str)
        self.assertEqual(err[1], '40400')

    def test_err_patients_autocomplete_internal_server_error_ok(self):
        err = getattr(error, 'ERR_PATIENTS_AUTOCOMPLETE_INTERNAL_SERVER_ERROR')
        self.assertEqual(type(err), tuple)
        self.assertEqual(len(err), 2)
        self.assertEqual(type(err[0]), str)
        self.assertEqual(err[0], 'internal server error')
        self.assertEqual(type(err[1]), str)
        self.assertEqual(err[1], '50000')


if __name__ == '__main__':
    unittest.main()