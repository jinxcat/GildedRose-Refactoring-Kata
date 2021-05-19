# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from texttest_fixture import item_set

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_name_remains_same(self):
        # set of items tested
        items = item_set
        # expected item set output
        expected_items = item_set

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for i in range(len(items)):
            self.assertEquals(expected_items[i].name, items[i].name)

        
if __name__ == '__main__':
    unittest.main()
