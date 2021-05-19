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

    def test_quality_drops_twice_as_fast_for_expired_items(self):
        # set of items tested
        items = [
            Item("+5 Dexterity Vest", 10, 20),
            Item("+5 Dexterity Vest", 0, 20)
        ]
        # expected item set output
        expected = [
            {'sell_in': 9, 'quality': 19},
            {'sell_in': -1, 'quality': 18},
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

        
if __name__ == '__main__':
    unittest.main()
