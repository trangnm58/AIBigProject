with open('ai_lib/3_letters_dictionary') as open_file:
    m_dict = open_file.read().split()

def gen():
    for w1 in m_dict:
        for w2 in m_dict:
            for w3 in m_dict:
                if check(w1, w2, w3):
                    with open('inputs.txt', 'a') as myfile:
                        myfile.write(w1 + w2 + w3 + '\n')

def check(w1, w2, w3):
    if (check_word(w1[0] + w2[0] + w3[0])
    and check_word(w1[1] + w2[1] + w3[1])
    and check_word(w1[2] + w2[2] + w3[2])
    and check_word(w1[2] + w2[1] + w3[0])
    and check_word(w1[0] + w2[1] + w3[2])):
        return True

def check_word(w):
    return w in m_dict

gen()