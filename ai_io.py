import re


# read 2 given files once when this module is imported
with open('3_letters_dictionary') as open_file:
    letters_dict = open_file.read()
    
with open('bigram_frequence_list') as open_file:
    freq_list = open_file.read()


def read_input(file_name):
    """
    Input: string file_name
    Output: file's data as 2D list of letters
    """
    with open(file_name) as open_file:
        data = open_file.read()

    data = data.split()
    return [data[0:3], data[3:6], data[6:9]]

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

def print_result(letters):
    """
    Input: one 2D tuple or 2D list of letters
    Output: write to 'result.txt' file as 3x3 matrix
    """
    open_file = open("result", 'w')

    for i in letters:
        open_file.write(' '.join(i))
        open_file.write('\n')

