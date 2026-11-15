prompt = "\ntell me something, and i will repeat it back to you:"
prompt += "\nenter 'exit' to end the program. "

while True:
    city = input(prompt)
    if city == "exit":
        break
    else:
        print(f"i was born in {city.title()}")