import sys


def read_instance_file(f):
    n = int(f.readline())
    b = [float(x) for x in f.readline().split()]
    lines = []
    for i in range(n):
        tail = [int(x) for x in f.readline().split()]
        tail.append(i+1)
        lines.append(tail)
    return n, b, lines


def jureks_algorithm(b, tasks):
    machines = []
    print(tasks)
    for i in range(5):
        machines.append([b[i], 0])
    tasks.sort(key=lambda x: x[1] + x[0])
    print(tasks)

    result = [[], [], [], [], []]
    for task in tasks:
        task_p, task_r, task_i = task[0], task[1], task[2]
        wsp = [m[0] * m[1] for m in machines]
        best_wsp = min(wsp)
        for j in range(5):
            if machines[j][0] * machines[j][1] == best_wsp:
                machines[j][1] = max(machines[j][1], task_r) + task_p
                result[j].append(task_i)
                break
    return result


def check(n, b, instances, solutions):
    F = 0.00
    for i in range(5):
        time = 0.00
        for t in solutions[i]:
            p, r, null = instances[t-1]
            if r > time:
                time = r + (p * b[i])
            else:
                time += p * b[i]
            F += time - r
    F /= n
    F = round(F, 2)
    return F


def save_solution(n, F, result):
    outFile = open("132244-solution-{}.txt".format(n), "w")
    outFile.write(str(F) + '\n')
    for r in result:
        for index in r:
            outFile.write(str(index) + " ")
        outFile.write('\n')
    outFile.close()


if __name__ == '__main__':
    try:
        # inFiles = listdir('instances/')
        # read_more_files(inFiles)
        inFile = sys.argv[1]
        file = open(inFile, "r")
    except:
        print('Problem with opening file: no argument or no file. Quitting...')
        exit()

    n, b, tasks = read_instance_file(file)
    # print(f'{n} {b} {tasks}')
    result = jureks_algorithm(b, tasks.copy())
    # print(result)
    final = check(n, b, tasks, result)
    print(final)
    save_solution(n, final, result)
