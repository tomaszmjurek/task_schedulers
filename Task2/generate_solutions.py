from os import listdir
import sys
import os
import time

solutionsDir = "solutions_check/"
instancesDir = "instances_check/"

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

    instance = '132244-instance-'
    for i in range(50, 550, 50):
        command = f'{algorithm} {instance + str(i)}.txt'
        os.system(command)

    # print('Executing algorithm')
    # check_time = time.time()
    # os.system(command)
    # check_time = time.time() - check_time
    # print(f'Time = {check_time}')
    #
    # solutionFile = f'{algorithm[:6]}-solution-{n}.txt'
    # verify(instance, solutionFile)



if __name__ == '__main__':
    print("Started tester")
    verify_algorithm()
    read_results()

