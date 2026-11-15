pizza = {
    "crust": "pepperoni",
    "toppings": ["cheese","sossis","black olive"]
}

print(f"you ordered a {pizza['crust']}-crust pizza" 
       "with the following toppings")

for topping in pizza["toppings"]:
    print(f"\t{topping}")