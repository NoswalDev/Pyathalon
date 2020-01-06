#prompting and passing

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"How is the weather, {user_name}?")
weather = input(prompt)

print(f"{weather} weather is nice sometimes.")