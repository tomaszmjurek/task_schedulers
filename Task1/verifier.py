from os import listdir
import sys
import os
import time

solutionsDir = "solutions_check/"
instancesDir = "instances_check/"


def getSolutionIndexes(file):
    f = open(file) #solutionsDir +
    cost = int(f.readline())
    indexes = [int(x) for x in f.readline().split()]
    f.close()
    #print(indexes)
    return cost, indexes


def verify(file1, file2):
    f = open(instancesDir + file1)
    f.readline()
    lines = f.readlines()

    cost_to_compare, indexes = getSolutionIndexes(file2)
    time = 0
    cost_total = 0

    if len(indexes) != len(lines):
        print("Instance and solution count not match, I'm done")
        exit()

    for i in indexes:
        line = lines[i-1]
        p, r, d, w = [int(x) for x in line.split()]
        if r > time:
            time = r
        time += p
        if time > d:
            u = 1
        else:
            u = 0
        cost_total += u * w

    #print(f"cost read = {cost_to_compare}")
    print(f"cost = {cost_total}")
    if cost_to_compare == cost_total:
        print("\nOK")
    #else:
        #print("\nNOK")


def verify_files():
    solutionFiles = listdir(solutionsDir)
    instanceFiles = listdir(instancesDir)

    if len(solutionFiles) != len(instanceFiles):
        print("Instances and solutions number not match, I'm done")
        exit()

    for i in range(0, len(solutionFiles)):
        f1 = instanceFiles[i]
        f2 = solutionFiles[i]
        #print('Loaded instance ' + f1 + ' with solution ' + f2)
        verify(f1, f2)


def verify_algorithm():
    algorithm = sys.argv[1]
    instance = sys.argv[2]
    n = sys.argv[3]

    command = f'{algorithm} {instance}'

    print('Executing algorithm')
    check_time = time.time()
    os.system(command)
    check_time = time.time() - check_time
    print(f'Time = {check_time}')

    solutionFile = f'{algorithm[:6]}-solution-{n}.txt'
    verify(instance, solutionFile)


if __name__ == '__main__':
    print("Started verifier")

    #verify_files()
    verify_algorithm()

