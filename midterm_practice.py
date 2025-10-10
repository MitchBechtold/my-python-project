"""
#Problem 1
Create a restaurant order system with these functions:
1. add_to_order(order, item_name, quantity, price_per_item)
- Add item to order (or update quantity if exists)
- quantity must be positive integer
- price must be positive number
- Return True if successful, False otherwise
"""

def add_to_order(order, item_name, quantity, price_per_item):
    if quantity <= 0 or not isinstance(quantity, int):
        return False
    if price_per_item <= 0:
        return False
    if item_name in order:
        order[item_name]['quantity'] += quantity
    else:
        order[item_name] = {'quantity': quantity, 'price_per_item': price_per_item}
    return True
def remove_from_order(order, item_name):
    if item_name in order:
        del order[item_name]
        return True
    return False
def calculate_bill(order, tax_rate):
    subtotal = 0
    for item,  


"""
#Problem 2 
Track movie theater seat reservations using sets.
Write these functions:
1. reserve_seats(reservations, movie_name, seat_numbers)
- Reserve seats for a movie
- reservations: dict where keys are movie names, values are sets of reserved
seats
- seat_numbers: list of seat numbers to reserve
- Add movie if doesn't exist
"""
"""
def reserve_seats(reservations, movie_name, seat_numbers):
    if movie_name not in reservations:
        reservations[movie_name] = set()
    for seat in seat_numbers:
        reservations[movie_name].add(seat)
    return reservations[movie_name]
reservations = {}
reserve_seats(reservations, "Star Wars Episode IV", [1, 2, 3])
reserve_seats(reservations, "Star Wars Episode IV", [4, 5, 6])
reserve_seats(reservations, "Avatar", [1, 2, 3, 4])
print ("current reservations: " )
for movie, seats in reservations.items():
    print(f"{movie}: {sorted(seats)}")
"""