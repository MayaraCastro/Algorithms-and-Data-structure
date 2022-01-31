#  Have the function FirstReverse(str) take the str parameter being passed
#  and return the string in reversed order. For example: if the input string is "Hello World and Coders"
#  then your program should return the string sredoC dna dlroW olleH. 

def first_reverse(strParam):
  result = ''.join([strParam[i] for i in range(len(strParam)-1, -1, -1)])
  return result

print(first_reverse(input()))
