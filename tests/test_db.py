import unittest

from app import create_app, db, trie


class DBTestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app({
            'TESTING': True
        })

    def test_init_ok(self):
        result = db.init(self.app)
        data = getattr(db, '__dataset')
        self.assertEqual(type(data), dict)
        self.assertIn('patients', data)
        self.assertEqual(type(data['patients']), trie.Trie)

    def test_get_dataset(self):
        db.init(self.app)
        result = db.get_dataset('patients')
        self.assertEqual(type(result), trie.Trie)


if __name__ == '__main__':
    unittest.main()