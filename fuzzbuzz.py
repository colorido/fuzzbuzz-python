# coding: utf-8
# Here your code !

for num in range(1,101):
    if num % 15 == 0:
        print("fuzzbuzz")
    elif num % 3 == 0:
        print("fuzz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
