__author__ = 'aaronmsmith'

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total=0

for price in prices:
    total = total + (prices[price] * stock[price])

print total
