__author__ = 'aaronmsmith'

def hotel_cost(nights):
    cost=nights * 140
    return cost

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475

def rental_car_cost(days):
    cost=days*40

    if days>6:
        cost=cost-50
    elif days>2:
        cost =cost-20

    return cost

print hotel_cost(3)
print plane_ride_cost("Pittsburgh")
print rental_car_cost(7)
