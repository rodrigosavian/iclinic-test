import unittest

from app.patients import service


class ServiceTestClass(unittest.TestCase):

    def test_get_patients_by_name_ok(self):
        result = service.get_patients_by_name('mark')
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 2)

    def test_get_patients_by_name_empty_list(self):
        result = service.get_patients_by_name('notfound')
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()