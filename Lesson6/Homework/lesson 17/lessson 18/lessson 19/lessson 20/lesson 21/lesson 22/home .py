# دریافت عدد از کاربر (تبدیل به عدد صحیح با int)
number = int(input("enter a number: "))

#بررسی اینکه آیا عدد مضرب 10 است یا خیر 
if number % 10 == 0:
    print(number, "is a multiple of 10.")
else:
    print(number, "is not a multiple of 10.")