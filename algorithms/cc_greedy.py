import re
import heapq
import datetime

class CCGreedy:
    """docstring for CCGreedy"""
    F_BEFORE = [
        (),
        (0,),
        (1,),
        (0,),
        (0, 1, 2, 3),
        (2, 4),
        (3, 4),
        (4, 6),
        (4, 5, 7)
    ]

    F_AFTER = [
        (1, 3, 4),
        (2, 4),
        (4, 5),
        (4, 6),
        (5, 6, 7, 8),
        (8,),
        (7,),
        (8,),
        ()
    ]

    START_WORD = [3, 1, 2, 1, 0, 0, 1, 0, 0]

    M_BEFORE = [
        [],
        [],
        [(0, 1, 2)],
        [],
        [],
        [(3, 4, 5)],
        [(0, 3, 6), (2, 4, 6)],
        [(1, 4, 7)],
        [(0, 4, 8), (2, 5, 8), (6, 7, 8)]
    ]

    def __init__(self, inputs):
        self.inputs = inputs
        self.frequency_dicts = []
        self.results = []

        with open('ai_lib/3_letters_dictionary') as open_file:
            self.letters_dict = open_file.read()

        with open('ai_lib/bigram_frequence_list') as open_file:
            self.freq_list = open_file.read()

        for a_input in inputs:
            temp = {}
            for i in a_input:
                t_a_input = a_input[:]
                t_a_input.remove(i)
                for j in t_a_input:
                    temp[i+j] = self.get_frequency(i, j)
                temp['$'+i] = self.get_frequency('$', i)
            self.frequency_dicts.append(temp)

    def execute(self, trace, pause):
        for index, a_input in enumerate(self.inputs):
            start_time = datetime.datetime.now()
            state = 0
            matrix = []
            letters = a_input[:]
            heaps = []
            heaps.append(self.get_next_valid_letter(matrix, letters, index))

            while len(heaps) > 0:
                if trace:
                    print 'Current state: {}'.format(str(matrix))
                    print 'Parent: {}'.format(str(matrix[:len(matrix) - 1]))
                    print 'Depth: {}'.format(len(heaps))
                length = len(matrix)
                state += 1

                if length == 9:
                    if trace:
                        print 'Found result!'
                    end_time = datetime.datetime.now()
                    time = int((end_time - start_time).total_seconds() * 1000)
                    self.results.append((matrix, state, time))
                    del heaps[length]
                    break
                if length == 0 and len(heaps[0]) == 0:
                    if trace:
                        print 'Not found result!'
                    self.results.append(None)
                    break

                if len(heaps[length]) == 0:
                    if trace:
                        print 'Back to previous state.'
                    letters.append(matrix[length - 1])
                    del matrix[length - 1]
                    del heaps[length]
                else:
                    if trace:
                        print 'Children:'
                        for item in heaps[length]:
                            print '{}: h={}'.format(matrix + [item[1]], -item[0])
                    n_append = heapq.heappop(heaps[length])
                    matrix.append(n_append[1])
                    letters.remove(n_append[1])
                    heaps.append(self.get_next_valid_letter(matrix, letters, index))
                if pause:
                    wait = raw_input("Press Enter to continue!")

    def h(self, matrix, letters, letter, f_dict_index):
        """
        Input:
            matrix: 1D array of existed letters
            letters: 1D array of remain letters include letter
            letter: letter want to get h(letter)
            f_dict_index: index of used frequency_dict
        How-to-do:
            Calculate h for letter in matrix according to letters
        Output:
            double(h(letter)) bigger is better
        """
        index = len(matrix)
        h = 0
        t_letters = letters[:]
        t_letters.remove(letter)
        # Calcalate score for all frequency of letter before letter
        for i in CCGreedy.F_BEFORE[index]:
            h += self.frequency_dicts[f_dict_index][matrix[i] + letter]

        # Calcalate score for all frequency of letter after letter
        weight = len(CCGreedy.F_AFTER[index])
        for i in t_letters:
            h += weight * self.frequency_dicts[f_dict_index][letter + i]

        # Calcalate score for start word
        if CCGreedy.START_WORD[index] != 0:
            h += CCGreedy.START_WORD[index] * self.frequency_dicts[f_dict_index]['$' + letter]

        return h

    def has_meaning(self, *word):
        """
        Input:
            word is a tupple of 3 letters
        How-to-do:
            Search this word in dictionary
        Output:
            True: found in dictionary
            False: not found
        """
        j_word = ''.join(word)

        if re.search(j_word, self.letters_dict, re.I) == None:
            return False
        else:
            return True

    def get_frequency(self, *letters):
        """
        Input: a tuple of 2 letters named 'letters'
        Output: the frequency of those in the dictionary
        """
        if letters[0] != '$':
            pair = ' '.join(letters)
            line = re.search(pair + r'\s0.?[\d]*', self.freq_list, re.I).group()
        else:
            line = re.search('\$ ' + letters[1] + r'\s0.?[\d]*', self.freq_list, re.I).group()

        return float(line[4:])

    def get_next_valid_letter(self, matrix, letters, f_dict_index):
        """
        Input:
            matrix: 1D array of existed letters
            letters: 1D array of remain letters
        How-to-do:
            This is successor function will return all letters that can go into the next empty space on the path
        Output:
            A heap of pair(-h(letter), letter) minimun in the top of heap
            -h(letter) because bigger h is better so inverse them
            if letters has a letter twice or more return once
        """
        index = len(matrix)
        heap = []
        valided = []
        invalided = []

        for letter in letters:
            if letter not in invalided and letter not in valided:
                accept = True
                for w in CCGreedy.M_BEFORE[index]:
                    if not self.has_meaning(matrix[w[0]], matrix[w[1]], letter):
                        accept = False
                        invalided.append(letter)
                        break

                if accept:
                    heapq.heappush(heap, (-self.h(matrix, letters, letter, f_dict_index), letter))
                    valided.append(letter)

        return heap
