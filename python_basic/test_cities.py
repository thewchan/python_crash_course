import unittest
from city_country import city_country

class CityTestCase(unittest.TestCase):
    """Tests for city_country.py"""

    def test_city_country(self):
        """Do city names like 'Santiago, Chile' work?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """
        Do city names with population like 
        'Santiago, Chile - population 5000000' work?
        """
        formatted_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()