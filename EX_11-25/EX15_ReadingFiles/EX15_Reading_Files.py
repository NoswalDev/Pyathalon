

from sys import argv

script, target = argv

txt = open(target)

print(f"This is {target}:")
print(txt.read())

print("What's the target?")
file_again = input("> ")
txt_again = open(file_again)


print(txt_again.read())
