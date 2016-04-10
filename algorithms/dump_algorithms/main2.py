#========================
# Cat Can
# 2016/04/09
# Main program
#========================
import ai_lib.ai_io as io
import algorithms.cc_greedy as CC

def main():
    creat_new_input = raw_input("Create new set of input? [YN]: ")
    if creat_new_input == "" or creat_new_input.lower() == 'y':
        num_of_input = int(raw_input("How many?: "))
        io.create_input(num_of_input)
        print "Created {} inputs in file input".format(num_of_input)
    else:
        print "Use old inputs in file input"

    inputs = io.read_file("input")

    trace = raw_input("\nEnable tracing? [YN]: ")
    if trace == "" or trace.lower() == 'y':
        trace = True
    else:
        trace = False

    pause = raw_input("Execute step by step? [YN]: ")
    if pause == "" or pause.lower() == 'y':
        pause = True
    else:
        pause = False

    cc = CC.CCGreedy(inputs)
    cc.execute(trace, pause)

    results = []
    count = 0
    total_time = 0
    total_state = 0
    for item in cc.results:
        if item != None:
            count += 1
            total_state += item[1]
            total_time += item[2]
            results.append(''.join(item[0]))
        else:
            results.append("None")

    result_file = raw_input("\nWrite results to: ")
    io.print_results(results, result_file)
    print "\nThere are {} cases have result in {} cases".format(count, len(cc.results))
    if count > 0:
        print "Average"
        print "Time: {} miliseconds".format(total_time / count)
        print "State: {} states".format(total_state / count)

main()
