#========================
# Page Nguyen
# 2016/03/24
# Main program
#========================

import datetime
import collections

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper
import algorithms.pn_greedy_02 as pn_greedy_02
import algorithms.pn_greedy_03 as pn_greedy_03

# global
algorithms = collections.OrderedDict()
algorithms['1'] = pn_greedy_02
algorithms['2'] = pn_greedy_03


def main():
    creat_new_input = raw_input("Create new set of input? [Yn]: ")
    if creat_new_input == "" or creat_new_input.lower() == 'y':
        num_of_input = int(raw_input("How many?: "))
        ai_io.create_input(num_of_input)
    inputs = ai_io.read_input()

    print("Choose one of these algorithms to run:")
    for key, value in algorithms.items():
        print("{}. {}".format(key, value.__str__()))
    choice = raw_input("[{}]: ".format(''.join([i for i in algorithms.keys()])))

    trace = raw_input("Enable tracing? [Yn]: ")
    if trace == "" or trace.lower() == 'y':
        trace = True
    else:
        trace = False

    result_file = raw_input("Write results to: ")
    results = []

    time = 0
    for i in inputs:
        start_time = datetime.datetime.now()  # start time of 1 input
        result = algorithms[choice].main(i, trace)
        if result != False:
            end_time = datetime.datetime.now()  # end time of 1 input
            time += (end_time - start_time).total_seconds()
        results.append(result)

    ai_io.print_results(results, result_file)
    print("Finished in: {}".format(time))


main()

