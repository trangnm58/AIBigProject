import random
import copy

import ai_lib.ai_io as ai_io


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

def to_one_d(letters):
    """
    Input: 2D list or 2D tuple of letters
    Output: 1D list of letters
    """
    return [j for i in letters for j in i]

def to_two_d(letters):
    """
    Input: 1D list or 1D tuple of letters
    Output: 2D list of letters
    """
    return [letters[0:3], letters[3:6], letters[6:9]]

def get_frequency_list(letters):
    """
    Input: 2D list of letters
    Output: A list of tuple (key: value)
        key is a string of 2 letters from 'letters'
        value is a frequency of the 2 letters
    """
    OneD_letters = to_one_d(letters)
    fre_list = []
    for i in OneD_letters:
        lst_cp = OneD_letters[:]
        lst_cp.remove(i)
        for j in lst_cp:
            fre = ai_io.get_frequency(i, j)
            if fre > 0 and (i+j, fre) not in fre_list:
               fre_list.append((i+j, fre))
    # sort the list using bubble sort
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(fre_list) - 1):
            if fre_list[i][1] < fre_list[i+1][1]:
                fre_list[i], fre_list[i+1] = fre_list[i+1], fre_list[i]
                swapped = True
    return fre_list

def get_frequency_dict(letters):
    """
    Input: 2D list of letters
    Output: A dict of key-value
        key is a string of 2 letters from 'letters'
        value is a frequency of the 2 letters
    """
    OneD_letters = to_one_d(letters)
    fre_dict = {}
    for i in OneD_letters:
        lst_cp = OneD_letters[:]
        lst_cp.remove(i)
        for j in lst_cp:
            fre = ai_io.get_frequency(i, j)
            if fre > 0 and i+j not in fre_dict:
               fre_dict[i+j] = fre
    return fre_dict

