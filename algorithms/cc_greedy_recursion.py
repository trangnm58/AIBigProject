#========================
# Cat Can + Page Nguyen
# 2016/03/21
# Greedy algorithm find all possible permutations until the first result is found
#========================

import datetime

import lib.ai_io as ai_io
import lib.ai_helper as ai_helper


# global
met = [False]

def __str__():
    return 'cc_greedy_recursion'

def gen(letters, matrix, met):
    if len(letters) == 0:
        #print(matrix)  # uncomment this to see it run
        mtrx_cp = ai_helper.to_two_d(matrix)
        if ai_helper.check_all(mtrx_cp):
            met[0] = True
            return mtrx_cp
    else:
        for i in letters:
            temp = letters[:]
            temp.remove(i)
            matrix.append(i)
            gen(temp, matrix, met)
            if not met[0]:
                matrix.pop()
            else:
                return matrix

def main(letters):
    OneD_letters = ai_helper.to_one_d(letters)
    return gen(OneD_letters, [], met)

