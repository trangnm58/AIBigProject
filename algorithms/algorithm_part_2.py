import datetime

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper


class AlgorithmPart2:
    NAME = 'AlgorithmPart2'
    PREVIOUS = {1: 0, 2: 1, 3: 0, 4: 3, 5: 4, 6: 3, 7: 6, 8: 7}

    def __init__(self, inputs):
        self.inputs = inputs  # a list of n inputs
        self.results = []  # a list of n results

        # START: Find freq_dict for each input in inputs
        self.freq_dicts = []
        for i in self.inputs:
            self.freq_dicts.append(ai_helper.get_frequency_dict(i))
        # END

    def heuristic(self, state, index):
        score = 0

        if len(state) == 3:
            # check the first row
            if not ai_io.has_meaning(state[0], state[1], state[2]):
                # the first row has no meaning
                return 0
        elif len(state) == 6:
            # check the second row
            if not ai_io.has_meaning(state[3], state[4], state[5]):
                # the second row has no meaning
                return 0
        elif len(state) == 7:
            # check the first column and the right-left diagonal
            if (not ai_io.has_meaning(state[0], state[3], state[6])
                or not ai_io.has_meaning(state[2], state[4], state[6])):
                # first column and the right-left diagonal have no meanings
                return 0
        elif len(state) == 8:
            # check the second column
            if not ai_io.has_meaning(state[1], state[4], state[7]):
                # the second column has no meaning
                return 0
        elif len(state) == 9:
            # check the third column, the third row and the left-right diagonal
            if (not ai_io.has_meaning(state[2], state[5], state[8])
                or not ai_io.has_meaning(state[0], state[4], state[8])
                or not ai_io.has_meaning(state[6], state[7], state[8])):
                # the third column, the third row and the left-right diagonal have no meanings
                return 0

        # START: Accumulate the frequency of each pair of letters in 'state'
        for i in range(1, len(state)):
            try:
                # state[i] is the current letter
                # state[AlgorithmPart2.PREVIOUS[i]] is the letter that precedes state[i]
                freq = self.freq_dicts[index][state[AlgorithmPart2.PREVIOUS[i]] + state[i]]
            except Exception:
                continue
            else:
                score += freq
        # END
        return score

    def execute(self, trace, pause):
        # Loop through all inputs in 'inputs' list
        for i in range(len(self.inputs)):
            num_of_states = 0
            start_time = datetime.datetime.now()

            L = []  # a list of all states

            # START: Insert all letter in self.inputs[i] into L
            # this is where initial states are created
            for letter in self.inputs[i]:
                # get frequency of 'letter'
                freq = self.freq_dicts[i][letter]
                
                # insert (letter, freq) into L and keep L sorted
                if (letter, freq) not in L:
                    for j in range(len(L)):
                        if freq > L[j][1]:
                            L.insert(j, (letter, freq))
                            break
                    else:
                        L.append((letter, freq))
            # END

            while True:
                if len(L) == 0:
                    # can not find the result
                    self.results.append("None")
                    break

                current_state = L.pop(0)[0]
                
                # increment number of states
                num_of_states += 1

                if len(current_state) == 9:
                    # Found the result
                    end_time = datetime.datetime.now()
                    time = int((end_time - start_time).total_seconds() * 1000)
                    self.results.append((current_state, num_of_states, time))
                    break

                # START: Find a list of remaining letters (letters that are not in current_state)
                letters_left = self.inputs[i][:]
                for letter in current_state:
                    letters_left.remove(letter)
                # END

                if trace:
                    next_states = []

                for letter in letters_left:
                    next_state = current_state + letter
                    h_next = self.heuristic(next_state, i)  # the heuristic value of 'next_state'
                    if h_next == 0:
                        # skip the state if its heuristic value is 0
                        continue

                    # START: Insert 'next_state' into L and keep L sorted
                    if (next_state, h_next) not in L:
                        for j in range(len(L)):
                            if h_next > L[j][1]:
                                L.insert(j, (next_state, h_next))
                                break
                        else:
                            L.append((next_state, h_next))
                    # END

                    if trace:
                        next_states.append("H({}) = {}".format(next_state, h_next))

                if trace:
                    print("Current state: {}".format(current_state))
                    print("Depth: {}".format(len(current_state)))
                    print("Next states:")
                    for state in L:
                        print(state)
                    if pause:
                        try:
                            next = raw_input("Next?")
                        except:
                            next = input("Next?")

