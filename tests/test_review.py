#!/usr/bin/python3
"""Suite of unit tests for the Review class
"""
from models.review import Review
import datetime
import json
import unittest


class TestReviewAttributes(unittest.TestCase):
    """Performs tests on the attributes of an instance of Review
    """
    def test_check_attr_exist(self):
        """Checks for the existence of attributes
        """
        review = Review()

        # Inherited Attributes
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'created_at'))

        # Uninherited Attributes
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_check_attr_type(self):
        """Checks the type of each attribute
        """
        review = Review()

        # Inherited Attributes
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.updated_at, datetime.datetime)
        self.assertIsInstance(review.created_at, datetime.datetime)

        # Uninherited Attributes
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


class TestReviewMethods(unittest.TestCase):
    """Tests all the methods of the Review class
    """
    def test_to_dict(self):
        """Tests on the return value of the to_dict() method
        """
        review = Review()
        review.name = "Abuja"

        review_dict = review.__dict__.copy()
        review_dict['__class__'] = str(review.__class__.__name__)
        review_dict['created_at'] = review_dict['created_at'].isoformat()
        review_dict['updated_at'] = review_dict['updated_at'].isoformat()

        self.assertDictEqual(review_dict, review.to_dict())

    def test_save(self):
        """Tests on the save() method of the Review instance
        """
        review = Review()

        self.assertEqual(review.text, "")
        self.assertEqual(review.created_at, review.updated_at)

        review.false_text = 'This is a short review'
        self.assertEqual(review.false_text, 'This is a short review')
        self.assertEqual(review.created_at, review.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key in json_dict.keys():
            if review.id in key:
                break

        obj = json_dict[key]

        with self.assertRaises(KeyError):
            self.assertNotEqual(review.false_text, obj['false_text'])

        self.assertEqual(review.false_text, 'This is a short review')

        review.false_text = "Another review"
        review.save()
        self.assertEqual(review.false_text, "Another review")
        self.assertNotEqual(review.created_at, review.updated_at)

        with open('file.json', 'r') as file:
            json_dict = json.load(file)

        for key, value in json_dict.items():
            if review.id in key:
                break

        obj = json_dict[key]
        self.assertEqual(review.false_text, obj['false_text'])


if __name__ == '__main__':
    unittest.main()
