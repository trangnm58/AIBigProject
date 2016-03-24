#========================
# Page Nguyen
# 2016/03/17
# Heuristic algorithm based on total frequency score + number of words
#========================

import random
import copy
import datetime

import lib.ai_io as ai_io
import lib.ai_helper as ai_helper


def __str__():
    return 'pn_heuristic_01'

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

def main(letters):
    # read input
    letters_0 = letters

    while ai_helper.check_all(letters_0) == False:
        h_0 = heuristic(letters_0)

        letters_1 = ai_helper.swap_random(letters_0)

        count_inside = 0  # set the limit of inside loop
        while heuristic(letters_1) <= h_0 and count_inside < 5:
            letters_1 = ai_helper.swap_random(letters_0)
            count_inside += 1
        else:
            # letters_1 is better or loop exceeds 5 times
            # set letters_0 to whatever letters_1 currently is
            letters_0 = letters_1

    else:
        return letters_0

