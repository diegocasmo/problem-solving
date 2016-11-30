# Problem: https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/

from math import ceil

def solution(curr_position, final_position, jump_distance):
    return int(ceil((final_position - curr_position) / float(jump_distance)))
