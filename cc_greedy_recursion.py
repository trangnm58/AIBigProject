#========================
# Cat Can + Page Nguyen
# 2016/03/19
# Greedy algorithm find all possible permutations until the first result is found
#========================

import datetime

import ai_io


def check_all(letters1d):
    """
    Input: 1D array of letters
    Output: True of all words have meanings, False otherwise
    """
    letters = [['x','x','x'], ['x','x','x'], ['x','x','x']]
    
    letters[0][0] = letters1d[0]
    letters[0][1] = letters1d[1]
    letters[0][2] = letters1d[2]
    letters[1][0] = letters1d[3]
    letters[1][1] = letters1d[4]
    letters[1][2] = letters1d[5]
    letters[2][0] = letters1d[6]
    letters[2][1] = letters1d[7]
    letters[2][2] = letters1d[8]
    
    flag = True

    for i in range(0,3):
        # check row i and col i
        if (not ai_io.has_meaning(letters[i][0], letters[i][1], letters[i][2]) or
            not ai_io.has_meaning(letters[0][i], letters[1][i], letters[2][i])):
            flag = False
            break

    # check diagons
    if (not ai_io.has_meaning(letters[0][0], letters[1][1], letters[2][2]) or
        not ai_io.has_meaning(letters[0][2], letters[1][1], letters[2][0])):
        flag = False

    return flag

# global
met = [False]

def gen(letters, matrix, met):
    if not met[0]:
        if len(letters) == 0:
            # print(matrix)  # uncomment this to see it run
            if check_all(matrix):
                print(matrix)
                met[0] = True
        else:
            for i in letters:
                temp = letters[:]
                temp.remove(i)
                matrix.append(i)
                gen(temp, matrix, met)
                matrix.pop()

#main
start_time = datetime.datetime.now()  # start time
# run
gen(['a', 'e', 'o', 'p', 'r', 'r', 's', 'w', 'y'], [], met)
end_time = datetime.datetime.now()  # end time
print("Time: {}".format((end_time - start_time).total_seconds()))

