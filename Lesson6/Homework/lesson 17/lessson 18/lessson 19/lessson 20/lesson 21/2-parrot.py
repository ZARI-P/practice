prompt = "\ntell me something, and i will repeat it back to you:"
prompt += "\nenter 'exit' to end the program. "
message = ""
while message != "exit":
     message = input(prompt)
     if message != "exit":
         print(message)