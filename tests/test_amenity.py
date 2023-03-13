#!/usr/bin/python3
"""A suite of unit tests for the Amenity class
"""
from models.amenity import Amenity
import unittest
import datetime
import json


class TestAmenityNewInstance(unittest.TestCase):
    """Collection of tests for the different ways of creating a new Amenity
    instance
    """
    def testNoInstanceAttributes(self):
        """Tests on an instance created without any attributes passed
        to __init__
        """
        amenity = Amenity()
        amenity.name = "Wi-Fi"

        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

        self.assertIsInstance(amenity.name, str)

        self.assertEqual(amenity.updated_at, amenity.created_at)
        self.assertEqual(amenity.name, 'Wi-Fi')

    def testCreateInstanceWithKwargs(self):
        """Tests on an instance created with @**kwargs passed into
        __init__
        """
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        my_amenity_json = my_amenity.to_dict()
        my_new_amenity = Amenity(**my_amenity_json)

        self.assertIsNot(my_new_amenity, my_amenity)
        self.assertIsInstance(my_new_amenity, Amenity)
        self.assertIsInstance(my_new_amenity.id, str)
        self.assertIsInstance(my_new_amenity.created_at, datetime.datetime)
        self.assertIsInstance(my_new_amenity.updated_at, datetime.datetime)
        self.assertIsInstance(my_new_amenity.name, str)

        self.assertEqual(my_new_amenity.name, "Wi-Fi")

        self.assertEqual(my_new_amenity.created_at, my_new_amenity.updated_at)
        self.assertEqual(my_new_amenity.name, my_amenity.name)
        self.assertEqual(my_new_amenity.id, my_amenity.id)
        self.assertEqual(my_new_amenity.created_at, my_amenity.created_at)
        self.assertEqual(my_new_amenity.to_dict(), my_amenity.to_dict())


class TestAmenityMethods(unittest.TestCase):
    """Tests all the methods of the Amenity class
    """
    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        amenity = Amenity()
        amenity.name = "Julien"

        amenity_dict = amenity.__dict__.copy()
        amenity_dict['__class__'] = str(amenity.__class__.__name__)
        amenity_dict['created_at'] = amenity_dict['created_at'].isoformat()
        amenity_dict['updated_at'] = amenity_dict['updated_at'].isoformat()

        self.assertDictEqual(amenity_dict, amenity.to_dict())

    def test_save(self):
        """Tests on the save() method of the Amenity instance
        """
        amenity = Amenity()
        amenity.name = "Wi-Fi"

        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertEqual(amenity.created_at, amenity.updated_at)

        amenity.name = 'Cable'
        self.assertEqual(amenity.name, 'Cable')
        self.assertEqual(amenity.created_at, amenity.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if amenity.id in key:
                break

        obj = json_dict[key]

        with self.assertRaises(KeyError):
            self.assertEqual(amenity.name, obj['name'])

        self.assertEqual(amenity.name, 'Cable')

        amenity.name = "Air Conditioning"
        amenity.save()
        self.assertEqual(amenity.name, "Air Conditioning")
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if amenity.id in key:
                break

        obj = json_dict[key]
        self.assertEqual(amenity.name, obj['name'])


if __name__ == '__main__':
    unittest.main()
