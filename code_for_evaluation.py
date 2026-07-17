from typing import List, Optional
import sys

# Instructions:
# Please anaylze this code from me and joe. We know it's simple but
# we like it for our own reasons.
#
#
# Joe. I like this simple code for testing the debug stack. what do you
# think?
#

class BucketBuilder(object):
    def __init__(self) -> None:
        self.bucket: List[int] = []
    def add_item_to_the_bucket(self, item: int) -> List[int]:
        """
        Adds item to the objects bucket.
        
        Args:
            item (int): Item to add to the bucket.
        
        Returns:
            list
        """
        try:
            if not isinstance(item, int):
                raise TypeError("item must be an int")
            self.bucket.append(item)
            return self.bucket
        except TypeError as e:
            print(e, file=sys.stderr)

    def remove_from_the_bucket(self, item: int) -> List[int]:
        """
        Removes item to the objects bucket.
        
        Args:
            item (int): Item to remove to the bucket.
        
        Returns:
            list
        """
        try:
            if not isinstance(item, int):
                raise TypeError("item must be an int")
            if item not in self.bucket:
                raise ValueError(f'{item} not in bucket list')
            else:
                self.bucket = list(filter((item).__ne__, self.bucket))
            return self.bucket
        except Exception as e:
            print(e, file=sys.stderr)


def process_bucket(i: Optional[int]=None, adding: str='yes') -> List[int]:
    """
    Inserts and removes items from objects bucket.

    Args:
        i (Optional[int]): item to remove from list.
        adding (str): boolean str to check whether to add to list.
    
    Returns:
        list
    """
    b = BucketBuilder()

    for _z in range(10):
        if adding == 'yes':
            b.add_item_to_the_bucket(_z) # I like the bucket tracker
        else:
            if i is not None:
                b.remove_from_the_bucket(i)
    return b.bucket # Return the final accumulated bucket contents

import unittest, inspect
from inspect import signature

class TestBucketBuilder(unittest.TestCase):
    def setUp(self):
        self.bb = BucketBuilder()
        self.add_item = self.bb.add_item_to_the_bucket
        self.remove_item = self.bb.remove_from_the_bucket

    def test_bucketbuilder_attrs(self):
        self.assertTrue(hasattr(self.bb, 'bucket'))
        self.assertTrue(isinstance(self.bb.bucket, List))

    def test_add_item_to_the_bucket(self):
        self.assertIn('item', signature(self.add_item).parameters)
        self.assertTrue(signature(self.add_item).return_annotation, List)
        self.assertTrue(len(self.bb.bucket) < 1)
        self.bb.add_item_to_the_bucket(5)
        self.bb.add_item_to_the_bucket(67)
        self.assertTrue(len(self.bb.bucket) == 2)
        with self.assertRaises(TypeError):
            self.bb.add_item_to_the_bucket('5')
        self.assertTrue(len(self.bb.bucket) == 2)

    def test_remove_from_the_bucket(self):
        self.assertIn('item', signature(self.remove_item).parameters)
        self.assertTrue(signature(self.remove_item).return_annotation, List)
        self.bb.add_item_to_the_bucket(5)
        self.bb.add_item_to_the_bucket(88)
        self.bb.add_item_to_the_bucket(5)
        self.bb.add_item_to_the_bucket(5)
        self.assertTrue(len(self.bb.bucket) == 4)
        self.bb.remove_from_the_bucket(5)
        self.assertTrue(len(self.bb.bucket) == 1)

if __name__ == '__main__':
    print("Hello, world")
    b = process_bucket(adding='yes')
    print(b)
    for u in b:
        process_bucket(u, adding='no')
    print("Goodbye, world :')") # We need to ungreet the user only once.
