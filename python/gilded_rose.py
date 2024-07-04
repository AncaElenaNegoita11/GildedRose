# -*- coding: utf-8 -*-
import random


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

    def probability_fake(self, chance):
        return random.random() < chance

    def fibonacci(self, number):
        if number == 0 or number == 1:
            return number
        return self.fibonacci(number - 1) + self.fibonacci(number - 2)

    def verify_fake_item(self, item):
        if not item.fake and self.probability_fake(0.33):
            item.fake = True
            item.fake_days_fibo = 0

    def modify_fake_item(self, item):
        if item.fake:
            if item.sell_in > 0:
                item.quality = max(0, item.quality - self.fibonacci(item.fake_days_fibo))
            item.fake_days_fibo += 1

    def update_quality(self):
        for item in self.items:
            if not item.sell_in % 2:
                self.verify_fake_item(item)
            self.modify_fake_item(item)
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
    def __init__(self, name, sell_in, quality, fake, fake_days_fibo):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.fake = fake
        self.fake_days_fibo = fake_days_fibo

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
