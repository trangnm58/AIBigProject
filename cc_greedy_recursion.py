#========================
# Cat Can + Page Nguyen
# 2016/03/21
# Greedy algorithm find all possible permutations until the first result is found
#========================

import datetime

import ai_io
import ai_helper


# global
met = [False]

def gen(letters, matrix, met):
    if not met[0]:
        if len(letters) == 0:
            #print(matrix)  # uncomment this to see it run
            mtrx_cp = ai_helper.to_two_d(matrix)
            if ai_helper.check_all(mtrx_cp):
                print(mtrx_cp)
                met[0] = True
        else:
            for i in letters:
                temp = letters[:]
                temp.remove(i)
                matrix.append(i)
                gen(temp, matrix, met)
                matrix.pop()

def main():
    letters = ai_io.read_input('input01')
    OneD_letters = ai_helper.to_one_d(letters)
    gen(OneD_letters, [], met)

#main
start_time = datetime.datetime.now()  # start time
# run
main()
end_time = datetime.datetime.now()  # end time
print("Time: {}".format((end_time - start_time).total_seconds()))

