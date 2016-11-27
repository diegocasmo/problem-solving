# Problem: https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/start/

def solution(array):
  elements_count = get_elements_count(array)
  # Find first odd value occurrence in elements count dict
  for key, value in elements_count.iteritems():
    if is_odd(value):
      return key

# Given an array, return a dictionary which contains the array values as keys
# and the number of occurrences in the array as values
def get_elements_count(array):
  count = {}
  for element in array:
    if element in count:
      count[element] += 1
    else:
      count[element] = 1
  return count

# Return true if a number is odd, false otherwise
def is_odd(num):
    return num % 2 != 0
