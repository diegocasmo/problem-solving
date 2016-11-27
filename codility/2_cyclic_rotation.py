# Problem: https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/start/

def solution(array, num_of_rotations):
  if len(array) > 0:
      for _ in xrange(num_of_rotations):
        array = rotate_right(array)
  return array

# Rotate an array to the right once
def rotate_right(array):
  last_element = array.pop(len(array) - 1)
  return [last_element] + array
