numbers = list(range(1, 7))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#مربع اعداد کمتر از 10
sequars = []
for value in range(1, 11):
    sequar = value ** 2
    sequars.append(sequar)
    print(sequars)
    
    equars = []
for value in range(1, 11):
    sequar = value ** 2
    sequars.append(sequar)
    print(sequars)
    
    sequars = [value**2 for value in range(1, 11)]
    print (sequars)