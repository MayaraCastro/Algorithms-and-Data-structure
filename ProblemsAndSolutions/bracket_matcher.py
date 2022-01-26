# Have the function BracketMatcher(str) take the str parameter being passed 
# and return 1 if the brackets are correctly matched and each one is accounted for. 
# Otherwise return 0. For example: if str is "(hello (world))",
# then the output should be 1, but if str is "((hello (world))" the the output should be 0 
# because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. 
# If str contains no brackets return 1. 

def bracket_matcher(strParam):
  count = 0
  for char in strParam:
    if char == '(':
      count += 1
    elif char == ')':
      count -= 1
    if count < 0:
      return '0'
  return '0' if count else '1'

print(bracket_matcher(input()))
