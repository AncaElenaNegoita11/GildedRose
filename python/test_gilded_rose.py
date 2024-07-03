# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", 2, 10),
                 Item("Aged Brie", 8, 20)]
        aged_brie = GildedRose(items)
        aged_brie.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(7, items[1].sell_in)

    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 2, 10),
                 Item("Aged Brie", 8, 20)]
        aged_brie = GildedRose(items)
        aged_brie.update_quality()
        self.assertEqual(11, items[0].quality)
        self.assertEqual(21, items[1].quality)

    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80),
                 Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        sulfuras = GildedRose(items)
        sulfuras.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(0, items[1].sell_in)

    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80),
                 Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        sulfuras = GildedRose(items)
        sulfuras.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(80, items[1].quality)

    def test_backstage_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 2),
                 Item("Backstage passes to Electric Castle", 7, 30)]
        backstage = GildedRose(items)
        backstage.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(6, items[1].sell_in)

    def test_backstage_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 2),
                 Item("Backstage passes to Electric Castle", 7, 30)]
        backstage = GildedRose(items)
        backstage.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(32, items[1].quality)

    def test_conjured_sell_in(self):
        items = [Item("Conjured Morgana", 4, 2),
                 Item("Conjured Ragnaros", 12, 25)]
        backstage = GildedRose(items)
        backstage.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(11, items[1].sell_in)

    def test_conjured_quality(self):
        items = [Item("Conjured Morgana", 4, 2),
                 Item("Conjured Ragnaros", 12, 25)]
        backstage = GildedRose(items)
        backstage.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(23, items[1].quality)


if __name__ == '__main__':
    unittest.main()
