user_input = input("Enter some text:")
dct = {"a":"4", "b":"8", "e":"3", "l":"1", "o":"0", "s":"5", "t":"7"}
for key, value in dct.items():
    user_input = user_input.replace(key, value)

print(user_input)