req_toppings = ["tomato","mushrooms","cheese","olive","corn","pineapple"]
req ="apple","banana"
if req_toppings:
    for req in req_toppings:
        print(f"adding {req}")
        print("\nfinished making your pizza")
    else:
        print("you have not add toppings yet!!!")