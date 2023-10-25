def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost += -50
    elif d >= 3:
        cost += -20
    return cost

# P int
# R int total cost of renting the vehicle, there are discounts at 3+ day rentals and at 7+ day rentals
# E 4 = 140
# P use if else, with >= 7 being first in order