#========================
# Page Nguyen
# 2016/03/24
# Main program
#========================

import datetime
import collections

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper
from algorithms.pn_greedy_02 import PNGreedy


# algorithms is a ordered dict of key:value
   # key is a number: 1, 2, 3....
   # value is a imported class module
algorithms = collections.OrderedDict()
algorithms['1'] = PNGreedy  # PNGreedy is a class


def main():
    creat_new_input = raw_input("Create new set of input? [Yn]: ")
    if creat_new_input == "" or creat_new_input.lower() == 'y':
        num_of_input = int(raw_input("How many?: "))
        # create 'num_of_input' inputs in 'input' file
        ai_io.create_input(num_of_input)

    inputs = ai_io.read_input()  # a list of 'num_of_input' stored in 'input' file

    print("Choose one of these algorithms to run:")
    for key, value in algorithms.items():
        print("{}. {}".format(key, value.NAME))  # 'NAME' is static attribute of class 'value'
    choice = raw_input("[{}]: ".format(''.join([i for i in algorithms.keys()])))

    trace = raw_input("Enable tracing? [Yn]: ")
    if trace == "" or trace.lower() == 'y':
        trace = True
    else:
        trace = False

    # initialize algorithm object with 'inputs' list
    algorithm = algorithms[choice](inputs)
    # run it
    algorithm.execute(trace)

    print("Finished")


main()

