#========================
# Page Nguyen
# 2016/03/24
# Main program
#========================

import datetime
import collections

import ai_lib.ai_io as ai_io
import ai_lib.ai_helper as ai_helper
import algorithms.pn_greedy_recursion_01 as pn_greedy_recursion_01
import algorithms.pn_heuristic_01 as pn_heuristic_01
import algorithms.cc_greedy_recursion as cc_greedy_recursion


# global
algorithms = collections.OrderedDict()
algorithms['1'] = pn_greedy_recursion_01
algorithms['2'] = pn_heuristic_01
algorithms['3'] = cc_greedy_recursion

def main():
    file_name = input("Input file: input/")
    letters = ai_io.read_input("input/" + file_name)
    print("Choose one of these algorithms to run:")
    for key, value in algorithms.items():
        print("{}. {}".format(key, value.__str__()))
    choice = input("[{}]: ".format(''.join([i for i in algorithms.keys()])))
    
    start_time = datetime.datetime.now()  # start time
    print("Result: {}".format(algorithms[choice].main(letters)))
    end_time = datetime.datetime.now()  # end time
    print("Time: {}".format((end_time - start_time).total_seconds()))

#run
main()

