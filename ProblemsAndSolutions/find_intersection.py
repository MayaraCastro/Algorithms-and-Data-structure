# Have the function FindIntersection(strArr) read the array of strings 
# stored in strArr which will contain 2 elements: the first element 
# will represent a list of comma-separated numbers sorted in ascending order,
# the second element will represent a second list of comma-separated numbers (also sorted). 
# Your goal is to return a comma-separated string containing the numbers that occur in elements
# of strArr in sorted order.
# If there is no intersection, return the string false. 

def find_intersection(strArr):
  list1 = set([int(i) for i in strArr[0].split(",")])
  list2 = set([int(i) for i in strArr[1].split(",")])
  result = list(list1.intersection(list2))
  return ','.join([str(i) for i in sorted(result)]) if result else 'false'

print(find_intersection(input()))
