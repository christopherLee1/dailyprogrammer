"""Finds degree of garland words"""


def garland(s):
   degree = 0
   for i in range (0, len(s)):
      if s[:i] == s[-i:]:
         degree = max(degree, i)
   return degree

print('Example words:')
print('degree of \'onion\' = %d' % (garland('onion')))
print('degree of \'ceramic\' = %d' % (garland('ceramic')))
print('degree of \'alfalfa\' = %d\n' % (garland('alfalfa')))

word = input("Enter your own word:\n")
print('degree of \'%s\' = %d' % (word, garland(word)))