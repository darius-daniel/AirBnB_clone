#!/usr/bin/python3
"""Suite of tests for the Place class
"""
from models.place import Place
import datetime
import json
import unittest


class TestPlaceAttributes(unittest.TestCase):
    """Performs tests on the attributes of an instance of Place
    """
    def test_check_attr_exist(self):
        """Checks for the existence of attributes
        """
        place = Place()

        # Inherited Attributes
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'created_at'))

        # Uninherited Attributes
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guests'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_check_attr_type(self):
        """Checks the type of each attribute
        """
        place = Place()

        # Inherited Attributes
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.updated_at, datetime.datetime)
        self.assertIsInstance(place.created_at, datetime.datetime)

        # Uninherited Attributes
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guests, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)


class TestPlaceMethods(unittest.TestCase):
    """Tests all the methods of the Place class
    """
    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        place = Place()
        place.name = "Abuja"

        place_dict = place.__dict__.copy()
        place_dict['__class__'] = str(place.__class__.__name__)
        place_dict['created_at'] = place_dict['created_at'].isoformat()
        place_dict['updated_at'] = place_dict['updated_at'].isoformat()

        self.assertDictEqual(place_dict, place.to_dict())

    def test_save(self):
        """Tests on the save() method of the Place instance
        """
        place = Place()

        self.assertEqual(place.name, "")
        self.assertEqual(place.created_at, place.updated_at)

        place.false_name = 'Billy\'s Place'
        self.assertEqual(place.false_name, 'Billy\'s Place')
        self.assertEqual(place.created_at, place.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key in json_dict.keys():
            if place.id in key:
                break

        obj = json_dict[key]

        with self.assertRaises(KeyError):
            self.assertNotEqual(place.false_name, obj['false_name'])

        self.assertEqual(place.false_name, "Billy's Place")

        place.false_name = "Palace"
        place.save()
        self.assertEqual(place.false_name, "Palace")
        self.assertNotEqual(place.created_at, place.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if place.id in key:
                break

        obj = json_dict[key]
        self.assertEqual(place.false_name, obj['false_name'])


if __name__ == '__main__':
    unittest.main()
