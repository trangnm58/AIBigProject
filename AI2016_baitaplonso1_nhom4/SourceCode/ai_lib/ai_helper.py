import random
import copy

import ai_lib.ai_io as ai_io


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

def get_frequency_dict(letters):
    """
    Input: 1D list of letters
    Output: A dict of key-value
        key is a string of 2 letters or 1 letter from 'letters'
        value is a frequency of the 2 letters or 1 letter
    """
    freq_dict = {}
    # START: Find frequency of 1 letter
    for i in letters:
        freq = ai_io.get_frequency('$', i)
        if freq > 0 and '$'+i not in freq_dict:
            freq_dict[i] = freq
    # END
    # START: Find frequency of 2 letters
    for i in letters:
        letters_cp = letters[:]
        letters_cp.remove(i)
        for j in letters_cp:
            freq = ai_io.get_frequency(i, j)
            if freq > 0 and i+j not in freq_dict:
               freq_dict[i+j] = freq
    # END
    return freq_dict

