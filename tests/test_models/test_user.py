#!/usr/bin/python3
"""Suite of unittests for the User class
"""
import unittest
import json
from models.user import User
import datetime


class TestUserNewInstance(unittest.TestCase):
    """Collection of tests for the different ways of creating a new User
    instance
    """
    def testNoInstanceAttributes(self):
        """Tests on an instance created without any attributes passed
        to __init__
        """
        user = User()
        user.first_name = "Julien"
        user.last_name = "Barbier"
        user.password = '1234'
        user.email = 'julienb@holbertonschool.com'

        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime.datetime)
        self.assertIsInstance(user.updated_at, datetime.datetime)

        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

        self.assertEqual(user.updated_at, user.created_at)
        self.assertEqual(user.email, 'julienb@holbertonschool.com')
        self.assertEqual(user.password, '1234')
        self.assertEqual(user.first_name, 'Julien')
        self.assertEqual(user.last_name, "Barbier")

    def testCreateInstanceWithKwargs(self):
        """Tests on an instance created with @**kwargs passed into
        __init__
        """
        my_user = User()
        my_user.first_name = "Julien"
        my_user.last_name = "Barbier"
        my_user.password = '1234'
        my_user.email = 'julienb@holbertonschool.com'
        my_user_json = my_user.to_dict()
        my_new_user = User(**my_user_json)

        self.assertIsNot(my_new_user, my_user)
        self.assertIsInstance(my_new_user, User)
        self.assertIsInstance(my_new_user.id, str)
        self.assertIsInstance(my_new_user.created_at, datetime.datetime)
        self.assertIsInstance(my_new_user.updated_at, datetime.datetime)
        self.assertIsInstance(my_new_user.first_name, str)
        self.assertIsInstance(my_new_user.last_name, str)
        self.assertIsInstance(my_new_user.email, str)
        self.assertIsInstance(my_new_user.password, str)

        self.assertEqual(my_new_user.first_name, "Julien")
        self.assertEqual(my_new_user.last_name, "Barbier")
        self.assertEqual(my_new_user.password, '1234')
        self.assertEqual(my_new_user.email, 'julienb@holbertonschool.com')

        self.assertEqual(my_new_user.created_at, my_new_user.updated_at)
        self.assertEqual(my_new_user.first_name, my_user.first_name)
        self.assertEqual(my_new_user.last_name, my_user.last_name)
        self.assertEqual(my_new_user.password, my_user.password)
        self.assertEqual(my_new_user.email, my_user.email)
        self.assertEqual(my_new_user.id, my_user.id)
        self.assertEqual(my_new_user.created_at, my_user.created_at)
        self.assertEqual(my_new_user.to_dict(), my_user.to_dict())


class TestUserMethods(unittest.TestCase):
    """Tests all the methods of the User class
    """
    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        user = User()
        user.first_name = "Julien"
        user.last_name = "Barbier"
        user.password = '1234'
        user.email = 'julienb@holbertonschool.com'

        user_dict = user.__dict__.copy()
        user_dict['__class__'] = str(user.__class__.__name__)
        user_dict['created_at'] = user_dict['created_at'].isoformat()
        user_dict['updated_at'] = user_dict['updated_at'].isoformat()

        self.assertDictEqual(user_dict, user.to_dict())

    def test_save(self):
        """Tests on the save() method of the User instance
        """
        user = User()
        user.first_name = "Julien"
        user.last_name = "Barbier"
        user.password = '1234'
        user.email = 'julienb@holbertonschool.com'

        self.assertEqual(user.first_name, "Julien")
        self.assertEqual(user.created_at, user.updated_at)

        user.first_name = 'Alfred'
        self.assertEqual(user.first_name, 'Alfred')
        self.assertEqual(user.created_at, user.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if user.id in key:
                break

        obj = json_dict[key]

        with self.assertRaises(KeyError):
            self.assertEqual(user.first_name, obj['first_name'])

        self.assertEqual(user.first_name, 'Alfred')

        user.first_name = "Guillaume"
        user.save()
        self.assertEqual(user.first_name, "Guillaume")
        self.assertNotEqual(user.created_at, user.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if user.id in key:
                break

        obj = json_dict[key]
        self.assertEqual(user.first_name, obj['first_name'])


if __name__ == '__main__':
    unittest.main()
