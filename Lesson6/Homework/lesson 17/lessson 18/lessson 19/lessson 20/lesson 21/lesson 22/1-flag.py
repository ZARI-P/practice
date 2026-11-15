prompt = "\ntell me something, and i will repeat it back to you:"
prompt += "\nenter 'exit' to end the program. "

active = True

while active:
    message = input(prompt)
    if message == "exit":
        active = False
    else:
        print(message)