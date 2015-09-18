# coding: utf-8

print [ "fuzzbuzz" if not x % 15 else
            "fuzz" if not x % 3 else
            "buzz" if not x % 5 else
            x for x in range(1,101)]
