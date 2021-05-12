import sys
from operator import itemgetter


def read_more_files(inFiles):
    if len(inFiles) == 0:
        print('No files in folder instances\nNothing to do...')
        exit()

    for file in inFiles:
        print(f"Reading file {file}")
        inFile = open("instances/" + file, "r")
        read_file(inFile)


def read_file(f):
    n = int(f.readline())

    lines = f.readlines()
    tasks = []

    for i in range(len(lines)):
        line = lines[i]
        p, r, d, w = [int(x) for x in line.split()]
        task = [i, p, r, d, w]
        tasks.append(task)

    f.close()
    #print('Instance file read successfully')
    return n, tasks


# tasks[i, p, r, d, w]
def jurek_algorithm(tasks):
    result = []
    T_bad = []
    time = 0

    wsp = [t[1] / t[4] for t in tasks]
    T = [x for _, x in sorted(zip(wsp, tasks))] # sorted w/p

    while T:
        for t in T:
            if max(t[2], time) + t[1] > t[3]:
                T_bad.append(t[0])
                T.remove(t)

        if len(T) == 0: break
        min_r = min(t[2] for t in T)

        for t in T:
            r = t[2]
            if r == min_r:
                result.append(t[0])
                T.remove(t)
                time = max(time, r) + t[1]
                break

    result.extend(T_bad)
    return result


def calculate_cost(tasks, indexes):
    cost_total, time = 0, 0
    for i in indexes:
        x, p, r, d, w = tasks[i]
        if r > time:
            time = r
        time += p
        if time > d:
            u = 1
        else:
            u = 0
        cost_total += u * w

    return cost_total


def save_result_to_file(n, c, result):
    outFile = open("132244-solution-{}.txt".format(n), "w")
    outFile.write(str(c) + '\n')
    for r in result:
        outFile.write(str(r) + " ")
    outFile.close()
    #print('Solution file generated successfully')


if __name__ == '__main__':
    #print("Started 132244 algorithm")
    try:
        # inFiles = listdir('instances/')
        # read_more_files(inFiles)
        inFile = sys.argv[1]
        file = open(inFile, "r")
    except:
        print('Problem with opening file: no argument or no file. Quitting...')
        exit()

    n, tasks = read_file(file)
    result_indexes = jurek_algorithm(tasks)
    cost = calculate_cost(tasks, result_indexes)
    save_result_to_file(n, cost, [x+1 for x in result_indexes])
    #print('Finished 132244 algorithm')