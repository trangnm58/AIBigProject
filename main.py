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
algorithms['1'] = AlgorithmPart2
algorithms['2'] = AlgorithmPart3

def main():
    try:
        # python version is 2.x
        input_func = raw_input
    except:
        # python version is 3.x
        input_func = input

    creat_new_input = input_func("Create new set of input? [Yn]: ")
    if creat_new_input == "" or creat_new_input.lower() == 'y':
        num_of_input = int(input_func("How many?: "))
        # get random 'num_of_input' from input library
        # put 'num_of_input' inputs in 'input' file
        ai_io.create_input(num_of_input)
        print("{} inputs is generated in file 'input'\n".format(num_of_input))
    else:
        print("Use old inputs in file 'input'\n")

    # read inputs
    inputs = ai_io.read_input()  # a list of 'num_of_input' stored in 'input' file

    # select algorithm to run
    print("Choose one of these algorithms to run:")
    for key, value in algorithms.items():
        print("{}. {}".format(key, value.NAME))  # 'NAME' is static attribute of class 'value'
    choice = input_func("[{}]: ".format(''.join([i for i in algorithms.keys()])))

    # setup
    print("\nNote: Running in Tracing mode effects the time but not the number of states")
    trace = input_func("Enable tracing? [yN]: ")
    if trace.lower() == 'y':
        trace = True
    else:
        trace = False

    pause = False
    if trace:
        pause = input_func("Execute step by step? [Yn]: ")
        if pause == "" or pause.lower() == 'y':
            pause = True
        else:
            pause = False

    # initialize algorithm object with 'inputs' list
    algorithm = algorithms[choice](inputs)
    # run the algorithm
    print("Please wait!")
    algorithm.execute(trace, pause)

    # caculate the result performance according to the returned results
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

    # Write result to file and print the performance to screen
    result_file = input_func("\nWrite results to: ")
    if result_file != "":
        ai_io.print_results(results, result_file)
    print("\nThere are {} cases have result in {} cases".format(count, len(algorithm.results)))
    if count > 0:
        print("Average")
        print("Time: {} miliseconds".format(total_time / count))
        print("State: {} states".format(total_state / count))


main()

