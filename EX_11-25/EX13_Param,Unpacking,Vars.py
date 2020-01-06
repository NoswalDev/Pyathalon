#THis doesn't work because when I run it, I don't type in extra shit. If I did type extra shit such as: python3.8 ex13.py one two, This would pull out all those items and assign them to variables


from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)