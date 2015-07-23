#! usr/bin/env python3

"""
Shuffle a list using the Faro shuffle. Given a list of
space separated values, return a shuffled list.
Different calls should generate different lists.
Because of the nature of the Faro shuffle the first element
of the list and last element of the list will be the same
after shuffling.
"""

"""Uncomment the random.shuffle(vowels) to get a
randomized input, which actually shuffles a list as well"""

import random
random.seed()

def faroShuffle(l):
   s = []
   top = None
   if len(l) % 2 != 0:
      top = l[(len(l)-1)]
   a = l[0:len(l)//2]
   b = l[len(l)//2:]
   for (key1, key2) in zip(a,b):
      s.append(key1)
      s.append(key2)
   if top:
      s.append(top)

   return s

"""
Shuffle a list using the Fisher-Yates shuffle. Given a list of
space separated values, return a shuffled list.
Different calls should generate different lists.
"""

def fisherYatesShuffle(l):
   for i in range(len(l)-1,1,-1):
      j = random.randint(0,i)
      l[i], l[j] = l[j], l[i] # swap elems
   return l

v = input("Enter a space separated list:\n")
vowels = v.split()
# random.shuffle(vowels)
print("Original List: %s" % vowels)
print("Shuffled by Faro Shuffle: %s" % faroShuffle(vowels))
print("Shuffled by Fisher-Yates Shuffle: %s" % fisherYatesShuffle(vowels))