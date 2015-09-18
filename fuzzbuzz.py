# coding: utf-8

for num in range(1,101):
    if not num % 15:
        print "fuzzbuzz"
    elif not num % 3:
        print "fuzz"
    elif not num % 5:
        print "buzz"
    else:
        print num
