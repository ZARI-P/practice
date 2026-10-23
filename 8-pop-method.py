trucks = ['scania', 'volvo', 'benz', 'daf']
print(trucks)

popped_truck = trucks.pop(2)
print(trucks)

last_owned_truck = trucks.pop(0)
print(f"The last truck i owned was a {last_owned_truck.upper()}")
print(trucks)