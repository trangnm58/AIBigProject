import re


# read 2 given files once when this module is imported
with open('3_letters_dictionary') as open_file:
    letters_dict = open_file.read()
    
with open('bigram_frequence_list') as open_file:
    freq_list = open_file.read()


def read_input(file_name):
    """
    Input: string file_name
    Output: file's data as string
    """
    with open(file_name) as open_file:
        return open_file.read()

def has_meaning(*letters):
    """
    Input: a tuple of 3 letters named 'letters'
    Output: True if it has a meaning, False otherwise
    """
    word = ''.join(letters)

    if re.search(word, letters_dict, re.I) == None:
        return False
    else:
        return True

def get_frequency(*letters):
    """
    Input: a tuple of 2 letters named 'letters'
    Output: the frequency of those in the dictionary
    """
    pair = ' '.join(letters)

    line = re.search(pair + r'\s0[\d.]*', freq_list, re.I).group()

    return float(line[4:])

