# Have the function LongestWord(sen) take the sen parameter being passed 
# and return the longest word in the string. If there are two or more words
# that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty. 
# Words may also contain numbers, for example "Hello world123 567" 

import re

def longest_word(sen):
  words = re.findall('(\w+)', sen)
  longest = words[-1]
  for i in range(len(words) - 2, -1, -1):
    if len(words[i]) >= len(longest):
      longest = words[i]
  return longest

print(longest_word(input()))
