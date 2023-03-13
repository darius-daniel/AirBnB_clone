#!/usr/bin/python3
"""Suite of tests for the State class
"""
from models.state import State
import datetime
import json
import unittest


class TestStateNewInstance(unittest.TestCase):
    """Collection of tests for the different ways of creating a new State
    instance
    """
    def testNoInstanceAttributes(self):
        """Tests on an instance created without any attributes passed
        to __init__
        """
        state = State()
        state.name = "Wi-Fi"

        self.assertIsInstance(state, State)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)

        self.assertIsInstance(state.name, str)

        self.assertEqual(state.updated_at, state.created_at)
        self.assertEqual(state.name, 'Wi-Fi')

    def testCreateInstanceWithKwargs(self):
        """Tests on an instance created with @**kwargs passed into
        __init__
        """
        my_state = State()
        my_state.name = "Wi-Fi"
        my_state_json = my_state.to_dict()
        my_new_state = State(**my_state_json)

        self.assertIsNot(my_new_state, my_state)
        self.assertIsInstance(my_new_state, State)
        self.assertIsInstance(my_new_state.id, str)
        self.assertIsInstance(my_new_state.created_at, datetime.datetime)
        self.assertIsInstance(my_new_state.updated_at, datetime.datetime)
        self.assertIsInstance(my_new_state.name, str)

        self.assertEqual(my_new_state.name, "Wi-Fi")

        self.assertEqual(my_new_state.created_at, my_new_state.updated_at)
        self.assertEqual(my_new_state.name, my_state.name)
        self.assertEqual(my_new_state.id, my_state.id)
        self.assertEqual(my_new_state.created_at, my_state.created_at)
        self.assertEqual(my_new_state.to_dict(), my_state.to_dict())


class TestStateMethods(unittest.TestCase):
    """Tests all the methods of the State class
    """
    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        state = State()
        state.name = "Julien"

        state_dict = state.__dict__.copy()
        state_dict['__class__'] = str(state.__class__.__name__)
        state_dict['created_at'] = state_dict['created_at'].isoformat()
        state_dict['updated_at'] = state_dict['updated_at'].isoformat()

        self.assertDictEqual(state_dict, state.to_dict())

    def test_save(self):
        """Tests on the save() method of the State instance
        """
        state = State()
        state.name = "Wi-Fi"

        self.assertEqual(state.name, "Wi-Fi")
        self.assertEqual(state.created_at, state.updated_at)

        state.name = 'Cable'
        self.assertEqual(state.name, 'Cable')
        self.assertEqual(state.created_at, state.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if state.id in key:
                break

        obj = json_dict[key]

        with self.assertRaises(KeyError):
            self.assertEqual(state.name, obj['name'])

        self.assertEqual(state.name, 'Cable')

        state.name = "Air Conditioning"
        state.save()
        self.assertEqual(state.name, "Air Conditioning")
        self.assertNotEqual(state.created_at, state.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if state.id in key:
                break

        obj = json_dict[key]
        self.assertEqual(state.name, obj['name'])


if __name__ == '__main__':
    unittest.main()
