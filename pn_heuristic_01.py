#========================
# Page Nguyen
# 2016/03/17
# Heuristic algorithm based on total frequency score + number of words
#========================

import random
import copy
import datetime

import ai_io


def swap_random(letters):
    """
    Input: 2D list of letters
    Output: 2D list of letters that has 2 positions different from input
    """
    row1 = random.randint(0, 2)
    col1 = random.randint(0, 2)
    row2 = random.randint(0, 2)
    col2 = random.randint(0, 2)

    while row2 == row1 and col2 == col1:
        # random the same position
        # random again
        row2 = random.randint(0, 2)

    # swap 2 letters at 2 positions
    letters_cp = copy.deepcopy(letters)
    letters_cp[row1][col1], letters_cp[row2][col2] = letters_cp[row2][col2], letters_cp[row1][col1]
    
    return letters_cp

def heuristic(letters):
    """
    Input: 2D tuple or 2D list of letters
    Output: sum of frequencies plus number of meaningful words
    """
    score = 0

    for i in range(0,3):
        # accumulate by rows
        score += ai_io.get_frequency(letters[i][0], letters[i][1])
        score += ai_io.get_frequency(letters[i][1], letters[i][2])
        if ai_io.has_meaning(letters[i][0], letters[i][1], letters[i][2]):
            # row i has meaning
            score += 1

        # accumulate by cols
        score += ai_io.get_frequency(letters[0][i], letters[1][i])
        score += ai_io.get_frequency(letters[1][i], letters[2][i])
        if ai_io.has_meaning(letters[0][i], letters[1][i], letters[2][i]):
            # column i has meaning
            score += 1

    #accumulate by diagonals
    score += ai_io.get_frequency(letters[0][0], letters[1][1])
    score += ai_io.get_frequency(letters[1][1], letters[2][2])
    if ai_io.has_meaning(letters[0][0], letters[1][1], letters[2][2]):
        # diagonal left - right has meaning
        score += 1
    score += ai_io.get_frequency(letters[0][2], letters[1][1])
    score += ai_io.get_frequency(letters[1][1], letters[2][0])
    if ai_io.has_meaning(letters[0][2], letters[1][1], letters[2][0]):
        # diagonal right - left has meaning
        score += 1

    return score

def check_all(letters):
    """
    Input: 2D tuple or 2D list of letters
    Output: True of all words have meanings, False otherwise
    """
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
    
def main():
    # read input
    letters_0 = ai_io.read_input('input01')

    while check_all(letters_0) == False:
        h_0 = heuristic(letters_0)

        letters_1 = swap_random(letters_0)

        count_inside = 0  # set the limit of inside loop
        while heuristic(letters_1) <= h_0 and count_inside < 5:
            letters_1 = swap_random(letters_0)
            count_inside += 1
        else:
            # letters_1 is better or loop exceeds 5 times
            # set letters_0 to whatever letters_1 currently is
            letters_0 = letters_1

    else:
        # print to file
        ai_io.print_result(letters_0)
        print("Result: {}".format(letters_0))


start_time = datetime.datetime.now()  # start time
# run
main()
end_time = datetime.datetime.now()  # end time
print("Time: {}".format((end_time - start_time).total_seconds()))

