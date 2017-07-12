

import unittest
import app

class ViewTest(unittest.TestCase):
    '''Basic app tests'''
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        '''Test home page route'''
        response = self.app.get('/', follow_redirects=True)
        print(response.data)
        self.assertEqual(response.status_code, 200)
