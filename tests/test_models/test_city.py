#!/usr/bin/python3
"""Suite of tests for the City class
"""
from models.city import City
import datetime
import json
import unittest

class TestCityNewInstance(unittest.TestCase):
    """Collection of tests for the different ways of creating a new City
    instance
    """
    def testNoInstanceAttributes(self):
        """Tests on an instance created without any attributes passed
        to __init__
        """
        city = City()
        city.name = "Addis Ababa"

        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)

        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

        self.assertEqual(city.updated_at, city.created_at)
        self.assertEqual(city.name, 'Addis Ababa')

    def testCreateInstanceWithKwargs(self):
        """Tests on an instance created with @**kwargs passed into
        __init__
        """
        my_city = City()
        my_city.name = "Cape Town"
        my_city_json = my_city.to_dict()
        my_new_city = City(**my_city_json)

        self.assertIsNot(my_new_city, my_city)
        self.assertIsInstance(my_new_city, City)
        self.assertIsInstance(my_new_city.id, str)
        self.assertIsInstance(my_new_city.created_at, datetime.datetime)
        self.assertIsInstance(my_new_city.updated_at, datetime.datetime)
        self.assertIsInstance(my_new_city.name, str)
        self.assertTrue(hasattr(my_new_city, 'state_id'))
        self.assertIsInstance(my_new_city.state_id, str)

        self.assertEqual(my_new_city.name, "Cape Town")
        self.assertEqual(my_city.state_id, my_new_city.state_id)

        self.assertEqual(my_new_city.created_at, my_new_city.updated_at)
        self.assertEqual(my_new_city.name, my_city.name)
        self.assertEqual(my_new_city.id, my_city.id)
        self.assertEqual(my_new_city.created_at, my_city.created_at)
        self.assertEqual(my_new_city.to_dict(), my_city.to_dict())


class TestCityMethods(unittest.TestCase):
    """Tests all the methods of the City class
    """
    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        city = City()
        city.name = "Abuja"

        city_dict = city.__dict__.copy()
        city_dict['__class__'] = str(city.__class__.__name__)
        city_dict['created_at'] = city_dict['created_at'].isoformat()
        city_dict['updated_at'] = city_dict['updated_at'].isoformat()

        self.assertDictEqual(city_dict, city.to_dict())

    def test_save(self):
        """Tests on the save() method of the City instance
        """
        city = City()
        city.name = "Abuja"

        self.assertEqual(city.name, "Abuja")
        self.assertEqual(city.created_at, city.updated_at)

        city.name = 'Nairobi'
        self.assertEqual(city.name, 'Nairobi')
        self.assertEqual(city.created_at, city.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if city.id in key:
                break

        obj = json_dict[key]

        with self.assertRaises(KeyError):
            self.assertEqual(city.name, obj['name'])

        self.assertEqual(city.name, 'Cable')

        city.name = "Johannesburg"
        city.save()
        self.assertEqual(city.name, "Johannesburg")
        self.assertNotEqual(city.created_at, city.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if city.id in key:
                break

        obj = json_dict[key]
        self.assertEqual(city.name, obj['name'])


if __name__ == '__main__':
    unittest.main()
