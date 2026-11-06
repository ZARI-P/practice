age =1

if age < 4:
  print("your admission cost in 0t")
elif age < 18:
   print("your admission cost in 25t")
else:
    print("your admission cost in 65t") 
     
    if age < 4:
        price = "free"
    elif age < 18:
        price = 25
    elif age < 65:
        price = 50
    elif age >=65:
        price = 20
        
        print (f"your admission cost in {price}")