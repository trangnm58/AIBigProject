import datetime

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper


class AlgorithmPart3:
    """
    Description: This algorithm serves part 3's requirements.
    """
    NAME = 'AlgorithmPart3'
    PREVIOUS = {
        1: [0],
        2: [1],
        3: [0],
        4: [0, 1, 2, 3],
        5: [2, 4],
        6: [3, 4],
        7: [4, 6],
        8: [4, 5, 7]
    }

    def __init__(self, inputs):
        self.inputs = inputs  # a list of n inputs
        self.results = []  # a list of n results

        # START: Find freq_dict for each input in inputs
        self.freq_dicts = []
        for i in self.inputs:
            self.freq_dicts.append(ai_helper.get_frequency_dict(i))
        # END

    def heuristic(self, state, index):
        """
        Input:
            'state': the current state that need to evaluate heuristic value
            'index': the index of input in 'self.inputs'
        Output:
            The heuristic value of state
        """
        score = 0

        # START: Find a list of remaining letters (letters that are not in 'state')
        letters_left = self.inputs[index][:]
        for letter in state:
            letters_left.remove(letter)
        # END

        len_state = len(state)
        weight = 1.0/30.0

        if len_state == 2:
            # START: add score for each letter left which makes the first row has meaning
            for letter in letters_left:
                if ai_io.has_meaning(state[0], state[1], letter):
                    score += 0.001
                else:
                    try:
                        score += self.freq_dicts[index][state[0] + letter] * weight
                    except Exception:
                        pass
            # END

        elif len_state == 3 or len_state == 4:
            # check the first row
            if len_state == 3 and not ai_io.has_meaning(state[0], state[1], state[2]):
                # the first row has no meaning
                return 0
            else:
                score += 0.001  # score of the first row
                for letter in letters_left:
                    now_score = score  # the score before add 'letter' to 'state'
                    for j in AlgorithmPart3.PREVIOUS[len_state]:
                        try:
                            score += self.freq_dicts[index][state[j] + letter] * weight
                        except Exception:
                            # this 'letter' does not have a frequency with one of the previous letters
                            score = now_score  # reset score
                            break

        elif len_state == 5:
            # START: add score for each letter left which makes the second row has meaning
            for letter in letters_left:
                if ai_io.has_meaning(state[3], state[4], letter):
                    score += 0.001
                    for j in AlgorithmPart3.PREVIOUS[len_state]:
                        try:
                            score += self.freq_dicts[index][state[j] + letter] * weight
                        except Exception:
                            score -= 0.001
                            break
            # END

        elif len_state == 6:
            # check the second row
            if not ai_io.has_meaning(state[3], state[4], state[5]):
                # the second row has no meaning
                return 0
            else:
                # START: add score for each letter left which makes
                # the first column and the right-left diagonal has meaning
                for letter in letters_left:
                    if (ai_io.has_meaning(state[0], state[3], letter)
                        and ai_io.has_meaning(state[2], state[4], letter)):
                        score += 0.002
                # END
                if score == 0:
                    return 0

        elif len_state == 7:
            # check the first column and the right-left diagonal
            if (not ai_io.has_meaning(state[0], state[3], state[6])
                or not ai_io.has_meaning(state[2], state[4], state[6])):
                # first column and the right-left diagonal have no meanings
                return 0
            else:
                # START: add score for each letter left which makes the second column has meaning
                for letter in letters_left:
                    if ai_io.has_meaning(state[1], state[4], letter):
                            score += 0.004
                # END
                return score

        elif len_state == 8:
            # check the second column
            if not ai_io.has_meaning(state[1], state[4], state[7]):
                # the second column has no meaning
                return 0
            else:
                # START: add score for 1 letter left which makes
                # the third column, the third row and the left-right diagonal has meaning
                if (ai_io.has_meaning(state[2], state[5], letters_left[0])
                    and ai_io.has_meaning(state[0], state[4], letters_left[0])
                    and ai_io.has_meaning(state[6], state[7], letters_left[0])):
                    # this is the result
                    return 10
                else:
                    return 0
                # END

        # START: Accumulate the frequency of each pair of letters in 'state'
        for i in range(1, len_state):
            for j in AlgorithmPart3.PREVIOUS[i]:
                try:
                    # state[i] is the current letter
                    # state[j] is one of the letters that precedes state[i]
                    freq = self.freq_dicts[index][state[j] + state[i]] * weight
                except Exception:
                    return 0
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

                # START: Find a list of remaining letters (letters that are not in current_state)
                letters_left = self.inputs[i][:]
                for letter in current_state:
                    letters_left.remove(letter)
                # END

                if len(current_state) == 8:
                    # Found the result
                    end_time = datetime.datetime.now()
                    time = int((end_time - start_time).total_seconds() * 1000)
                    self.results.append((current_state + letters_left[0], num_of_states, time))
                    break

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

