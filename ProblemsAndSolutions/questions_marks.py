# Have the function QuestionsMarks(str) take the str string parameter,
# which will contain single digit numbers, letters, and question marks, 
# and check if there are exactly 3 question marks between every pair of 
# two numbers that add up to 10. If so, then your program should return the string true,
# otherwise it should return the string false. If there aren't any two numbers that add up to 10 
# in the string, then your program should return false as well.

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there
# are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string. 


import re
def questions_marks(strParam):
  pattern = '(\d)([\?|a-z]*)(\d)'
  matcher = re.compile(pattern);

  start = 0;
  string = strParam[start::]
  match = matcher.search(string)
  matches = []      
  while match: 
    matches.append(match)
    start = match.span()[1] -1
    string = string[start::]
    match = matcher.search(string)
  
  hasThreeMarks = False
  for match in matches:
    if int(match.group(1)) + int(match.group(3)) == 10:
      if not len(re.findall('(\?)', match.group(2))) == 3:
        return False
      else:
        hasThreeMarks = True
  return hasThreeMarks

print(questions_marks(input()))
