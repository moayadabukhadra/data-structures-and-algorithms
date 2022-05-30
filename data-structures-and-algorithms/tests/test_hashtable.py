from data_structures_and_algorithms.hashtable.hashtable import HashaTable,repeated_word,left_join
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


def test_repeated_words():
    actual = repeated_word("Once upon a time, there was a brave princess who...")
    expected="a"
    assert actual==expected

def test_repeated_words_edge_case():
    actual = repeated_word("hello")
    expected="hello"
    assert actual==expected

def test_left_join():
    Synonyms = HashaTable()
    Synonyms.set("diligent", "employed")
    Synonyms.set("fond", "enamored")
    Synonyms.set("guide", "usher")
    Synonyms.set("outfit", "garb")
    Synonyms.set("wrath", "anger")

    Antonyms =HashaTable()
    Antonyms.set("diligent", "idle")
    Antonyms.set("fond", "averse")
    Antonyms.set("guide", "follow")
    Antonyms.set("flow", "jam")  
    Antonyms.set("wrath", "delight")

    actual=left_join(Synonyms.map,Antonyms.map)
    expected=[['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    assert actual==expected








class Testhashtable(unittest.TestCase):
    def test_repeated_word_edge_case_two(self):
        with self.assertRaises(Exception):
            repeated_word(5)

    def test_left_join_edge_case_one(self):
        with self.assertRaises(Exception):
            hashtable=HashaTable()
            left_join(5,hashtable.map)
        
    def test_left_join_edge_case_two(self):
        with self.assertRaises(Exception):
            hashtable=HashaTable()
            left_join(hashtable.map,5)