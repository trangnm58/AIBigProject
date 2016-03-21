#========================
# Page Nguyen
# 2016/03/21
# Greedy algorithm find all possible permutations until the first result is found (used frequence_list)
#========================

import datetime

import ai_io
import ai_helper


# global
met = [False]
priv = {1: 0, 2: 1, 3: 0, 4: 3, 5: 4, 6: 3, 7: 6, 8: 7}

def gen(letters, matrix, met, fre_dict):
    if not met[0]:
        if len(matrix) == 9:
            #print(matrix)  # uncomment this to see it run
            mtrx_cp = ai_helper.to_two_d(matrix)
            if ai_helper.check_all(mtrx_cp):
                print(mtrx_cp)
                met[0] = True
        else:
            if len(matrix) == 0:
                for i in letters:
                    temp = letters[:]
                    temp.remove(i)
                    matrix.append(i)
                    gen(temp, matrix, met, fre_dict)
                    matrix.pop()
            else:
                pri = priv[len(matrix)]
                for i in letters:
                    if i in fre_dict[matrix[pri]]:
                        temp = letters[:]
                        temp.remove(i)
                        matrix.append(i)
                        gen(temp, matrix, met, fre_dict)
                        matrix.pop()

def main():
    letters = ai_io.read_input('input01')
    OneD_letters = [j for i in letters for j in i]
    fre_dict = ai_helper.get_frequency_dict(OneD_letters)
    gen(OneD_letters, [], met, fre_dict)


start_time = datetime.datetime.now()  # start time
# run
main()
end_time = datetime.datetime.now()  # end time
print("Time: {}".format((end_time - start_time).total_seconds()))

