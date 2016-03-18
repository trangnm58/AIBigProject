import random

import ai_io


def check_all(letters1d):
    """
    Input: 1D array of letters
    Output: True of all words have meanings, False otherwise
    """
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


met = False

def gen(letters, matrix):
    if not met:
        if len(letters) == 0:
            met = check_all(matrix)
        else:
            for i in letters:
                letters.remove(i)
                matrix.append(i)
                gen(letters, matrix)

gen(["x"]*9, [])
print(met)
     
