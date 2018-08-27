import unittest

from app.patients import constant


class ConstantTestClass(unittest.TestCase):

    def test_err_patients_autocomplete_queryparam_q_required_ok(self):
        const = getattr(constant, 'VALIDATE_PATIENTS_AUTOCOMPLETE_QUERYPARAM_Q_MIN_LENGTH')
        self.assertEqual(type(const), int)
        self.assertEqual(const, 2)


if __name__ == '__main__':
    unittest.main()