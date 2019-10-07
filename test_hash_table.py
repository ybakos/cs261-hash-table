# DO NOT MODIFY THE TESTS IN THIS FILE
# Run me via: python3 -m unittest test_hash_table

import unittest
import time
import random
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A HashTable exists.
        """
        try:
            HashTable()
        except NameError:
            self.fail("Could not instantiate HashTable.")

    # def test_size(self):
    #     """
    #     A default HashTable has a size attribute that is 10.
    #     """
    #     h = HashTable()
    #     self.assertEqual(10, h.size)

    # def test_instantiation_with_size(self):
    #     """
    #     A HashTable can be instantiated with an optional size.
    #     """
    #     h = HashTable(33)
    #     self.assertEqual(33, h.size)

    # """
    # Basic API
    # """

    # def test_simple_insertion(self):
    #     h = HashTable()
    #     try:
    #         h['foo'] = 'bar'
    #     except TypeError:
    #         self.fail("HashTable has no __setitem__ implementation")

    # def test_simple_retrieval(self):
    #     h = HashTable()
    #     try:
    #         _ = h['foo']
    #     except TypeError:
    #         self.fail("HashTable has no __getitem__ implementation")

    # def test_hash(self):
    #     """
    #     Hash function returns hash no greater than its size - 1.
    #     """
    #     h = HashTable(33)
    #     self.assertEqual(0, h.hash(0))
    #     self.assertEqual(32, h.hash(32))
    #     self.assertEqual(0, h.hash(33))
    #     self.assertEqual(1, h.hash(34))
    #     self.assertEqual(hash("fake key") % 33, h.hash("fake key"))

    # """
    # Data Storage
    # """

    # def test_data(self):
    #     """
    #     A HashTable has an internal array for storing k-v pairs.
    #     """
    #     h = HashTable()
    #     self.assertEqual(list, type(h.data))

    # def test_data_contents(self):
    #     """
    #     A HashTable data array contains empty lists.
    #     """
    #     h = HashTable(3)
    #     expected = [ [], [], [] ]
    #     self.assertEqual(expected, h.data)

    # """
    # Insertion Basics
    # """

    # def test_insert_one(self):
    #     """
    #     Inserting a k-v pair stores it as a two-element array in the list at
    #     the right index.
    #     """
    #     h = HashTable(3)
    #     h[11] = 'bar' # 11 is the key, not an index :)
    #     self.assertEqual([[11, 'bar']], h.data[2])

    # """
    # Retrieval Basics
    # """

    # def test_retrieve_none(self):
    #     """
    #     Retreiving a value for non-existent key returns None.
    #     """
    #     h = HashTable(3)
    #     self.assertEqual(None, h['foo'])

    # def test_retrieve_one(self):
    #     """
    #     The value of an inserted k-v pair is retrievable.
    #     """
    #     h = HashTable(3)
    #     h['foo'] = 'bar'
    #     self.assertEqual('bar', h['foo'])

    # """
    # Insertion
    # """

    # def test_insert_two(self):
    #     """
    #     Inserting two k-v pairs stores them as two-element arrays in the list
    #     at the right index.
    #     """
    #     h = HashTable(3)
    #     h[9] = 'foo' # Using numbers as keys for visibility.
    #     h[11] = 'bar'
    #     self.assertEqual([[9, 'foo']], h.data[0])
    #     self.assertEqual([[11, 'bar']], h.data[2])

    # def test_insert_existing(self):
    #     """
    #     Inserting a k-v pair where the key already exists overwrites the old value.
    #     """
    #     h = HashTable(3)
    #     h[9] = 'foo' # Using numbers as keys for visibility.
    #     h[9] = 'bar'
    #     self.assertEqual([[9, 'bar']], h.data[0])

    # def test_insert_collision(self):
    #     """
    #     Inserting a k-v pair where the key has the same hash as an existing key
    #     appends the new k-v pair to the list at the appropriate index.
    #     """
    #     h = HashTable(3)
    #     h[9] = 'foo'
    #     h[3] = 'bar'
    #     self.assertEqual([[9, 'foo'], [3, 'bar']], h.data[0])

    # """
    # Deletion
    # """

    # def test_delete(self):
    #     """
    #     Inserting a k-v pair where the key has the same hash as an existing key
    #     appends the new k-v pair to the list at the appropriate index.
    #     """
    #     h = HashTable(3)
    #     h['foo'] = 'bar'
    #     h.delete('foo')
    #     self.assertEqual(None, h['foo'])

    # """
    # Misc. Methods
    # """

    # def test_clear(self):
    #     """
    #     A cleared HashTable has an empty data array.
    #     """
    #     h = HashTable(3)
    #     h['foo'] = 'bar'
    #     h.clear()
    #     self.assertEqual([[], [], []], h.data)

    # def test_initial_keys(self):
    #     """
    #     A HashTable initially has no keys.
    #     """
    #     h = HashTable()
    #     self.assertEqual([], h.keys())

    # def test_keys(self):
    #     """
    #     A HashTable can produce a list of its keys.
    #     """
    #     h = HashTable()
    #     h['foo'] = 'bar'
    #     h['baz'] = 'qux'
    #     keys = h.keys()
    #     keys.sort()
    #     self.assertEqual(['baz', 'foo'], keys)


    # def test_initial_values(self):
    #     """
    #     A HashTable initially has no values.
    #     """
    #     h = HashTable(3)
    #     self.assertEqual([], h.values())

    # def test_values(self):
    #     """
    #     A HashTable can produce a list of its values.
    #     """
    #     h = HashTable()
    #     h['foo'] = 'bar'
    #     h['baz'] = 'qux'
    #     values = h.values()
    #     values.sort()
    #     self.assertEqual(['bar', 'qux'], values)

    # """
    # Time complexity
    # """

    # def test_retrieval_is_constant_time(self):
    #     """
    #     Retrieving a value from a dictionary should take the same amount of time
    #     no matter how many k-v pairs it contains. It should be O(... what?)
    #     """
    #     time_samples = []
    #     key = fake_key()
    #     value = fake_value()
    #     # Create a small hash table with just one k-v in it.
    #     small_table = HashTable()
    #     small_table[key] = value
    #     # Create a large hash table with 20,000 k-vs in it.
    #     large_table = HashTable(20000)
    #     for _ in range(10000):
    #         large_table[fake_key()] = fake_value()
    #     large_table[key] = value
    #     for _ in range(9999):
    #         large_table[fake_key()] = fake_value()
    #     # Calculate the average retrieval time for both small and large tables
    #     small_average_elapsed_time = average_retrieval_time(small_table, key)
    #     large_average_elapsed_time = average_retrieval_time(large_table, key)
    #     # Test that the average retrieval time for both small and large tables
    #     # is about the same.
    #     self.assertAlmostEqual(small_average_elapsed_time,\
    #         large_average_elapsed_time,\
    #         delta=small_average_elapsed_time*2) # Just a small amount, the 2 isn't significant.

    # def test_constant_retrieval_order(self):
    #     """
    #     Retrieving a value using the first-used key and the most recently-used
    #     key should be in constant time. (Order shouldn't matter.)
    #     """
    #     # Create a hash table with 20,000 entries in it.
    #     h = HashTable(20000)
    #     first_key = fake_key()
    #     last_key = fake_key()
    #     h[first_key] = fake_value()
    #     for _ in range(19998):
    #         h[fake_key()] = fake_value()
    #     h[last_key] = fake_value()
    #     # Calculate the average retrieval time for the first key and last key.
    #     first_key_value_average_retrieval_time = average_retrieval_time(h, first_key)
    #     last_key_value_average_retrieval_time = average_retrieval_time(h, last_key)
    #     # Test that the average retrieval time for both first and last keys
    #     # is about the same.
    #     self.assertAlmostEqual(first_key_value_average_retrieval_time,\
    #         last_key_value_average_retrieval_time,\
    #         delta=first_key_value_average_retrieval_time*2) # Just a small amount, the 2 isn't significant.

def fake_key():
    return f"FAKE KEY {time.time()}"

def fake_value():
    return f"FAKE VALUE {time.time()}"

def average_retrieval_time(table, key):
    time_samples = []
    for _ in range(1000):
        start_time = time.time()
        _ = table[key]
        end_time = time.time()
        time_samples.append(end_time - start_time)
    return sum(time_samples) / float(len(time_samples))

if __name__ == '__main__':
    unittest.main()
