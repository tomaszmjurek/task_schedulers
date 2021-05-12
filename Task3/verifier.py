import os
import time
from os import listdir
from sys import argv


def check(n, F_read, instances, solutions):
    D = 0.00
    W = 0
    time_m1, time_m2, time_m3 = 0, 0, 0
    for t in solutions:
        p1, p2, p3, d, w = instances[t-1]
        time_m1 += p1
        time_m2 = max(time_m1, time_m2) + p2
        time_m3 = max(time_m2, time_m3) + p3
        Dj = max(0, time_m3-d)
        D += (w * Dj)
        W += w
    D = D / W
    D = round(D, 2)
    print(f'{D}')
    if F_read != D:
        print('NOK: Solution and verifier D are different!')
        print(f'Read = {F_read} Calc = {D}')
    else:
        print('OK')
    return D


def read_instance_file(f):
    n = int(f.readline())
    lines = []
    for i in range(n):
        line = [int(x) for x in f.readline().split()]
        lines.append(line)
    return n, lines


def read_solution_file(f):
    F = float(f.readline())
    tasks = [int(x) for x in f.readline().split()]
    return F, tasks


def read_files(f1, f2):
    n1, instances = read_instance_file(f1)
    F, solutions = read_solution_file(f2)

    # if n1 != n2:
    #     print('Instance and solution n are different!')
    #     return
    check(n1, F, instances, solutions)


def read_many_files():
    # generate_solutions()
    solutionFiles = listdir('solutions_check/')
    instanceFiles = listdir('instances_check/')

    if len(solutionFiles) != len(instanceFiles):
        print("Instances and solutions number not match, I'm done")
        exit()

    for i in range(0, len(solutionFiles)):
        f1 = open('instances_check/' + instanceFiles[i], "r")
        f2 = open('solutions_check/' + solutionFiles[i], "r")
        read_files(f1, f2)


def verify_files(algorithm):
    cmd = f'{algorithm[0:6]}-solution-'
    finals = []

    for i in range(50, 550, 50):
        fileName = cmd + str(i) + '.txt'
        f = open(fileName, "r")
        D, tasks = read_solution_file(f)
        fileName = f'132244-instance-{i}.txt'
        f = open(fileName, "r")
        n, lines = read_instance_file(f)
        final = check(i, D, lines, tasks)
        finals.append(final)

    print(f'Results for {algorithm}')
    for fi in finals:
        print(fi)


def generate_solutions():
    instance = '132244-instance-'
    algorithm = argv[2]
    times = []
    for i in range(50, 550, 50):
        cmd = f'{algorithm} {instance + str(i)}.txt'
        print('Executing algorithm')
        check_time = time.time()
        os.system(cmd)
        check_time = time.time() - check_time
        micros_time = round(check_time * 100000)
        times.append(micros_time)
        print(f'Time = {micros_time}')
    print(f'Times for {algorithm}:')
    for t in times:
        print(t)

    verify_files(algorithm)


if __name__ == '__main__':
    try:
        inFileInstance = argv[1]
        if inFileInstance != 'many':
            inFileSolution = argv[2]
            f1 = open(inFileInstance, "r")
            f2 = open(inFileSolution, "r")
    except:
        print('Error reading files')
        exit()

    if inFileInstance == 'many':
        # read_many_files()
        generate_solutions()
    else:
        read_files(f1, f2)