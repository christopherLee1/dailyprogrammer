"""
from: https://www.reddit.com/r/dailyprogrammer/comments/3ddpms/20150715_challenge_223_intermediate_eel_of_fortune/
You work on the popular game show Eel of Fortune, where contestants take turns
fishing live eels out of an aquarium for the opportunity to solve a word puzzle.
The word puzzle works like the game Hangman. A secret word is obscured on the
board. A player guesses a letter of the alphabet, and if that letter appears
anywhere in the secret word, all of the times it appears in the secret word are
revealed.

An unfortunate incident occurred on yesterday's show. The secret word was
SYNCHRONIZED, and at one point the board was showing:

S _ N _ _ _ O N _ _ _ D

As you can see, the letters on the board spelled "snond", which is of course an
extremely offensive word for telemarketer in the Doldunian language. This
incident caused ratings to immediately plummet in East Doldunia. The Eel of
Fortune producers want the ability to identify "problem words" for any given
offensive word.

Write a function that, given a secret word and an offensive word, returns true
if the board could theoretically display the offensive word (with no additional
letters) during the course of solving the secret word.
"""


#my answer
def problem(mys_word, off_word):
   hang_list = []
   hang_word = ''
   for i in range(len(off_word)):
      index = mys_word.find(off_word[i])
      if index in hang_list: #find next instance
         index = mys_word.find(off_word[i], index+1)
      hang_list.append(index)
   hang_list = sorted(hang_list)
   for index in hang_list:
      hang_word += mys_word[index]
   if hang_word == off_word:
      return True
   else:
      return False

#subreddit python answer, so beautiful
def problem1(a, b):
   return b == ''.join(c for c in a if c in b)


print('\nMy Solution testing:')
#should print true
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('synchronized', 'snond', problem('synchronized', 'snond')))
#should print false
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('mispronounced', 'snond', problem('mispronounced', 'snond')))
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('shotgunned', 'snond', problem('shotgunned', 'snond')))
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('snond', 'snond', problem('snond', 'snond')))

print('\nElegant Answer testing:')
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('synchronized', 'snond', problem1('synchronized', 'snond')))
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('mispronounced', 'snond', problem1('mispronounced', 'snond')))
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('shotgunned', 'snond', problem1('shotgunned', 'snond')))
print('Mystery Word: \'%s\', Offensive word: \'%s\', %s' % ('snond', 'snond', problem1('snond', 'snond')))

#user input mys word and offensive word