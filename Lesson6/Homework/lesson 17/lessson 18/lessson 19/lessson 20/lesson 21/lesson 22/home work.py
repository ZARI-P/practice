white_list = ["niavaran","valanjak","zafaranieh","pasdaran","shahrak gharb"]
black_list = ["nasim shahr","hamdanak","orin","kheir abad","tajik"]

city = input("which city do you live in?")

if city in black_list and city not in white_list:
    print(city,"canceled")
else:
    print("let's be friends")