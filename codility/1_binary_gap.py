# Problem: https://codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(decimal_num):
  binary_string = transform_decimal_to_binary_string(decimal_num)
  return get_longest_binary_gap(binary_string)

# Transform a decimal number to a binary string
def transform_decimal_to_binary_string(decimal_num):
  return "{0:b}".format(decimal_num)

# Return longest binary gap in string
def get_longest_binary_gap(binary_string):
  longest_binary_gap = 0
  one_positions = get_one_positions_in_string(binary_string)
  if len(one_positions) > 1:
    for index, value in enumerate(one_positions):
      next_index = index + 1
      distance = (one_positions[next_index] - value) - 1 if next_index < len(one_positions) else 0
      longest_binary_gap = distance if distance > longest_binary_gap else longest_binary_gap
  return longest_binary_gap

# Return an array which contains the position of each 1 in the binary string
def get_one_positions_in_string(binary_string):
  one_positions = []
  for index, char in enumerate(binary_string):
    if char == '1':
      one_positions.append(index)
  return one_positions
