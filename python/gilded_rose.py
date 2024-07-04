# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Aged Brie":
                    # Increase quality until it reaches 50
                    item.quality = min(item.quality + 1, 50)
                case "Sulfuras, Hand of Ragnaros":
                    # Legendary item - no modifications
                    continue
                case item.name if item.name.startswith("Backstage passes"):
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
                case _:
                    power_increase = 1
                    # Conjured items take twice as much damage as an ordinary item
                    if item.name.startswith("Conjured"):
                        power_increase += 1
                    if item.sell_in > 0:
                        item.quality = max(0, item.quality - 1 * power_increase)
                    else:
                        item.quality = max(0, item.quality - 2 * power_increase)
            # Decrease the number of days left
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
