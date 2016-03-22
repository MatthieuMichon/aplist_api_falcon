"""Airport List Query web-API for Falcon WSGI Server module.

See:
https://github.com/MatthieuMichon/aplist_api_falcon
"""

import unittest

from aplist import AirportList


class AirportListDepTester(unittest.TestCase):
    """Test aplit depedency."""

    def setUp(self):
        """Test fixture setup."""
        self.al = AirportList()

    def test_simple_qeury(self):
        """Test simple query."""
        results = self.al.query(query={'search': {'icao': 'RJTT'}})
        self.assertEqual(len(results), 1)


if __name__ == '__main__':
    unittest.main()
