#!/usr/bin/python3
"""A Suite of tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelNewInstance(unittest.TestCase):
    """A suite of tests for the different methods of creating new instances
    of the BaseModel class
    """
    def testNoInstanceAttributes(self):
        """Tests on an instance created without any attributes passed
        to __init__
        """
        model = BaseModel()

        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)
        self.assertEqual(model.updated_at, model.created_at)

        self.assertEqual(len(model.id), 36)
        valid_ch = 'abcdefghijklmnopqrstuvwxyz0123456789-'

        for ch in model.id:
            self.assertIn(ch, valid_ch)

        fields = model.id.split('-')
        self.assertEqual(len(fields), 5)
        self.assertEqual(len(fields[0]), 8)
        self.assertEqual(len(fields[1]), 4)
        self.assertEqual(len(fields[2]), 4)
        self.assertEqual(len(fields[3]), 4)
        self.assertEqual(len(fields[4]), 12)

    def testCreateInstanceWithKwargs(self):
        """Tests on an instance created with @**kwargs passed into
        __init__
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertIsNot(my_new_model, my_model)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertIsInstance(my_new_model.id, str)
        self.assertIsInstance(my_new_model.created_at, datetime.datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime.datetime)
        self.assertEqual(my_new_model.created_at, my_new_model.updated_at)
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())


class TestBaseModelAttributes(unittest.TestCase):
    """A suite of tests for the attributes of the BaseModel class
    """
    my_model = BaseModel()

    def testBaseModel1(self):
        """ Test attributes value of a BaseModel instance """

        self.my_model.name = "ALX"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])


class TestBaseModelsMethods(unittest.TestCase):
    """Suite of tests for the methods of the BaseModel Class
    """
    my_model = BaseModel()

    def test_save(self):
        """ Checks if save method updates the public instance instance
        attribute updated_at """
        self.my_model.first_name = "First"
        self.my_model.save()

        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        model = BaseModel()
        model.first_name = "Julien"
        model.last_name = "Barbier"
        model.password = '1234'
        model.email = 'julienb@holbertonschool.com'

        model_dict = model.__dict__.copy()
        model_dict['__class__'] = str(model.__class__.__name__)
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()

        self.assertDictEqual(model_dict, model.to_dict())


if __name__ == '__main__':
    unittest.main()
