import unittest
from country_codes import get_country_code

class CCTestCase(unittest.TestCase):
    def test_code(self):
        code = get_country_code('China')
        self.assertEqual(code, 'cn')

unittest.main()