#!/usr/bin/env python3

"""
Based of of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders: [('apples', 1.0), ('oranges', 3.0)] best shop is shop1.
For orders: [('apples', 3.0)] best shop is shop2.
"""

import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """

    # *** Your Code Here ***
    best_shop = None
    best_price = float('inf')  # Initialize best_price to positive infinity

    for shop in fruitShops:
        total_price = 0
        for fruit, quantity in orderList:
            if fruit in shop.fruitPrices:
                total_price += shop.getCostPerPound(fruit) * quantity
            else:
                total_price = float('inf')  # If a shop doesn't have a fruit, it's not a valid choice
                break  # No need to continue checking this shop
        if total_price < best_price:
            best_price = total_price
            best_shop = shop

    return best_shop

def main():
    dir1 = {
        'apples': 2.0,
        'oranges': 1.0
    }

    dir2 = {
        'apples': 1.0,
        'oranges': 5.0
    }

    shop1 =  shop.FruitShop('shop1', dir1)
    shop2 = shop.FruitShop('shop2', dir2)

    shops = [shop1, shop2]

    orders = [('apples', 1.0), ('oranges', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

    orders = [('apples', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

if __name__ == '__main__':
    main()
