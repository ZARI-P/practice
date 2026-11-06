availabel_toppings =["tomato","mushrooms","cheese","olive","corn","pineapple"]

req_toppings = ["onion","black olive","meat","cheese"]

for req in req_toppings:
    if req in availabel_toppings:
        print(f"adding:{req}")
    else:
        print(f"sorry,we dont have this request {req}")
        
        print('\nfinished making your pizza!')