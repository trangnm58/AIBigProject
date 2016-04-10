#========================
# Page Nguyen
# 2016/03/24
# Main program
#========================

import datetime
import collections

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper
from algorithms.algorithm_part_2 import AlgorithmPart2
from algorithms.algorithm_part_3 import AlgorithmPart3


# algorithms is a ordered dict of key:value
   # key is a number: 1, 2, 3....
   # value is a imported class module
algorithms = collections.OrderedDict()
algorithms['1'] = AlgorithmPart2  # PNGreedy is a class
algorithms['2'] = AlgorithmPart3

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

    pause = False
    if trace:
        pause = raw_input("Execute step by step? [Yn]: ")
        if pause == "" or pause.lower() == 'y':
            pause = True

    # initialize algorithm object with 'inputs' list
    algorithm = algorithms[choice](inputs)
    # run it
    algorithm.execute(trace, pause)

    results = []
    count = 0
    total_time = 0
    total_state = 0
    for item in algorithm.results:
        if item != "None":
            count += 1
            total_state += item[1]
            total_time += item[2]
            results.append(''.join(item[0]))
        else:
            results.append("None")

    result_file = raw_input("\nWrite results to: ")
    if result_file != "":
        ai_io.print_results(results, result_file)
    print "\nThere are {} cases have result in {} cases".format(count, len(algorithm.results))
    if count > 0:
        print "Average"
        print "Time: {} miliseconds".format(total_time / count)
        print "State: {} states".format(total_state / count)


main()

