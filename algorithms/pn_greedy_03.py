#========================
# Page Nguyen
# 2016/04/05
#========================

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper


# global
previous = {1: 0, 2: 1, 3: 0, 4: 3, 5: 4, 6: 3, 7: 6, 8: 7}
# Cat's defined dict. Using this makes it run much longer
# {1: [0], 2: [1], 3: [0], 4: [0, 1, 2, 3], 5: [2, 4], 6: [3, 4], 7: [4, 6], 8: [4, 5, 7]}

def __str__():
    return 'pn_greedy_03'

def heuristic(state, freq_dict, letters):
    score = 0

    if len(state) == 3:
        if not ai_io.has_meaning(state[0], state[1], state[2]):
            return 0
    elif len(state) == 6:
        if not ai_io.has_meaning(state[3], state[4], state[5]):
            return 0
    elif len(state) == 7:
        if (not ai_io.has_meaning(state[0], state[3], state[6])
            or not ai_io.has_meaning(state[2], state[4], state[6])):
            return 0
    elif len(state) == 8:
        if not ai_io.has_meaning(state[1], state[4], state[7]):
            return 0
    elif len(state) == 9:
        if (not ai_io.has_meaning(state[2], state[5], state[8])
            or not ai_io.has_meaning(state[0], state[4], state[8])
            or not ai_io.has_meaning(state[6], state[7], state[8])):
            return 0

    for i in range(1, len(state)):
        try:
            freq = freq_dict[state[previous[i]] + state[i]]
        except Exception:
            continue
        else:
            score += freq

    # go deeper 1 move
    letters.remove(state[len(state) - 1])
    for letter in letters:
        try:
            freq = freq_dict[state[previous[len(state)]] + letter]
        except:
            continue
        else:
            score += freq
    return score

def greedy_heuristic(OneD_letters, freq_dict, trace):
    l = []

    for letter in OneD_letters:
        if (letter, 0) not in l:
            l.append((letter, 0))

    while True:
        if len(l) == 0:
            return False
        u = l.pop(0)[0]
        letters_cp = OneD_letters[:]  # copy of the original list of letters
        for i in u:
            letters_cp.remove(i)

        if len(u) == 9:
            return u

        if trace:
            next_states = []

        for letter in letters_cp:
            v = u + letter
            h_v = heuristic(v, freq_dict, letters_cp[:])

            if h_v == 0:
                # skip the state if its heuristic value is 0
                continue

            for i in range(len(l)):
                if h_v > l[i][1]:
                    l.insert(i, (v, h_v))
                    break
            else:
                l.append((v, h_v))
            if trace:
                next_states.append("H({}) = {}".format(v, h_v))

        if trace:
            print("Current state: {}".format(u))
            print("Level: {}".format(len(u)))
            print("Next states:")
            for state in next_states:
                print(state)

def main(letters, trace):
    OneD_letters = [j for i in letters for j in i]
    freq_dict = ai_helper.get_frequency_dict(OneD_letters)
    return greedy_heuristic(OneD_letters, freq_dict, trace)

