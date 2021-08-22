import random
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

sel_key, sel_value = random.choice(list(capitals_dict.items()))
sel_value = sel_value.lower()
while True:
    user_input = input(f"Please input the capital of {sel_key}:(type `exit` to exit.)").lower()
    if user_input == sel_value:
        print("Correct!")
        break
    if user_input == "exit":
        print(f"Correct answer is {sel_value}.\nGoodbye!")
        break
