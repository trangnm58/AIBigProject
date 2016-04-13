import re
import random


# read 3 given files once when this module is imported
with open('ai_lib/3_letters_dictionary') as open_file:
    letters_dict = open_file.read()

with open('ai_lib/bigram_frequence_list') as open_file:
    freq_list = open_file.read()

with open('ai_lib/inputs_dict') as open_file:
    inputs_dict = open_file.read().split()

def create_input(num_of_input):
    """
    Input: Number of inputs need to create
    Output: Print randomly created inputs to "input" file
    """
    inputs = []
    for k in range(num_of_input):
        ip = list(random.choice(inputs_dict))
        # rearrange order
        ip_reorder = ""
        for i in range(len(ip)):
            ip_reorder += random.choice(ip)
            ip.remove(ip_reorder[len(ip_reorder) - 1])
        inputs.append(ip_reorder)

    open_file = open("input", 'w')
    for i in inputs:
        open_file.write(i + "\n")

def read_input():
    """
    Output: a list of 1D list of letters
    """
    with open("input") as open_file:
        data = open_file.read()

    data = data.split()
    inputs = []
    for line in data:
        inputs.append(list(line))
    return inputs

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
    if letters[0] == '$':
        pair = '\\' + pair

    line = re.search(pair + r'\s0[\d.]*', freq_list, re.I).group()

    return float(line[4:])

def print_results(results, file_name):
    """
    Input: a list of strings of letters
    Output: write to file_name file as a string of 9 letters
    """
    open_file = open(file_name, 'w')

    for result in results:
        open_file.write(str(result) + "\n")

