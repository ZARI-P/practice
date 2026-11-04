squares =[i **2 for i in range(1, 11)]
print(squares)

even_squares =[num for num in squares if num % 2==0]
print (even_squares)

half_even_squares =[num /2 for num in even_squares]
print(half_even_squares)