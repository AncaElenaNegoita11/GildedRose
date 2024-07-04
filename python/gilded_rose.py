# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def aged_brie(self, item):
        # Increase quality until it reaches 50
        item.quality = min(item.quality + 1, 50)

    def backstage(self, item):
        # Increase the quality depending on the number of days left.
        # When the concert stops(no days left), quality becomes 0
        if item.sell_in > 0:
            if item.sell_in <= 5:
                item.quality += 3
            elif item.sell_in <= 10:
                item.quality += 2
            else:
                item.quality += 1
        else:
            item.quality = 0

    def conjured(self, item_name):
        power_increase = 1
        # Conjured items take twice as much damage as an ordinary item
        if item_name.startswith("Conjured"):
            power_increase += 1
        return power_increase

    def decrease_quality_ordinary(self, item, power_increase):
        if item.sell_in > 0:
            item.quality = max(0, item.quality - 1 * power_increase)
        else:
            item.quality = max(0, item.quality - 2 * power_increase)

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Aged Brie":
                    self.aged_brie(item)
                case "Sulfuras, Hand of Ragnaros":
                    # Legendary item - no modifications
                    continue
                case item.name if item.name.startswith("Backstage passes"):
                    self.backstage(item)
                case _:
                    power_increase = self.conjured(item.name)
                    self.decrease_quality_ordinary(item, power_increase)
            # Decrease the number of days left
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
