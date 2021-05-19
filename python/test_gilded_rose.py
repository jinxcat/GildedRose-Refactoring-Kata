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

    def test_expiration_and_quality_drop_for_normal(self):
        # set of items tested
        items = [
            Item("+5 Dexterity Vest", 10, 20),
            Item("+5 Dexterity Vest", 5, 10)
        ]
        # expected item set output
        expected = [
            {'sell_in': 9, 'quality': 19},
            {'sell_in': 4, 'quality': 9},
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    def test_quality_never_becomes_negative(self):
        # set of items tested
        items = [
            Item("+5 Dexterity Vest", 2, 1),
            Item("+5 Dexterity Vest", 1, 0),
            Item("+5 Dexterity Vest", -5, 0)
        ]
        # expected item set output
        expected = [
            {'sell_in': 1, 'quality': 0},
            {'sell_in': 0, 'quality': 0},
            {'sell_in': -6, 'quality': 0},
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

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

    def test_aged_brie_increases_quality_as_time_passes(self):
        self.skipTest("not implemented yet")
        pass

    def test_quality_is_never_above_50(self):
        self.skipTest("not implemented yet")
        pass

    def test_sulfuras_never_decreases_in_quality(self):
        self.skipTest("not implemented yet")
        pass

    def test_backstage_passes_increase_by_2_for_10_days_to_event(self):
        self.skipTest("not implemented yet")
        pass

    def test_backstage_passes_increase_by_3_for_5_days_to_event(self):
        self.skipTest("not implemented yet")
        pass

    def test_backstage_passes_to_zero_when_expired(self):
        self.skipTest("not implemented yet")
        pass

    def test_conjured_items_decrease_twice_as_fast_as_normal(self):
        self.skipTest("not implemented yet")
        pass

        
if __name__ == '__main__':
    unittest.main()
