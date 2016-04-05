#========================
# Page Nguyen
# 2016/04/05
#========================

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper


# global
priv = {1: 0, 2: 1, 3: 0, 4: 3, 5: 4, 6: 3, 7: 6, 8: 7}

def __str__():
    return 'pn_greedy_02'

def heuristic(state, fre_dict):
    score = 0
    for i in range(1, len(state)):
        score += fre_dict[state[priv[i]] + state[i]]
    return score

def greedy_heuristic(OneD_letters, fre_dict, trace):
    l = []
    for letter in OneD_letters:
        if (letter, 0) not in l:
            l.append((letter, 0))
    while True:
        if len(l) == 0:
            return False
        u = l.pop(0)[0]
        letters_cp = OneD_letters[:]
        for i in u:
            letters_cp.remove(i)
        if len(u) == 9:
            if ai_helper.check_all(ai_helper.to_two_d(list(u))):
                return u

        if trace:
            next_states = []

        for letter in letters_cp:
            try:
                check = fre_dict[u[priv[len(u)]] + letter]
            except:
                pass
            else:
                v = u + letter
                h_v = heuristic(v, fre_dict)
                for i in range(len(l)):
                    if h_v > l[i][1]:
                        l.insert(i, (v, h_v))
                        break
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
    fre_dict = ai_helper.get_frequency_dict(OneD_letters)
    return greedy_heuristic(OneD_letters, fre_dict, trace)

