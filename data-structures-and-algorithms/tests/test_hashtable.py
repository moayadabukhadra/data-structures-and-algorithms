from data_structures_and_algorithms.hashtable.hashtable import HashaTable
import unittest

def test_key_value_added_to_hashtable():
    hashtable=HashaTable()
    hashtable.set("key","value")
    if [["key","value"]] in hashtable.map:
        actual=True
    else:
        actual=False

    expected=True
    assert actual==expected

def test_get_returns_value_stored():
    hashtable=HashaTable()
    hashtable.set("key","value")
    actual=hashtable.get("key")
    expected="value"
    assert actual == expected

def test_get_returns_none():
    hashtable=HashaTable()
    actual=hashtable.get("key")
    expected=None
    assert actual == expected

def test_keys_returns_list_ofkeys():
    hashtable=HashaTable()
    hashtable.set("key","value")
    hashtable.set("key2","value2")
    actual=hashtable.keys()
    expected=['key2', 'key']
    assert actual == expected

def test_collision():
    hashtable=HashaTable()

    # two value with the same idx 
    hashtable.set("cat","value")
    hashtable.set("act","value2")

    idx=hashtable.hash("cat")
    actual=hashtable.map[idx]
    expected=[["cat","value"],["act","value2"]]
    assert actual==expected

def test_get_value_with_collision():
    hashtable=HashaTable()

    # two value with the same idx 
    hashtable.set("cat","value")
    hashtable.set("act","value2")

    idx=hashtable.hash("cat")
    actual=hashtable.get("cat")
    expected="value"
    assert actual==expected

def test_hashing_key_in_range():
    hashtable=HashaTable()
    actual=hashtable.hash("key")
    assert actual < 1024














class Testhashtable(unittest.TestCase):
    pass

