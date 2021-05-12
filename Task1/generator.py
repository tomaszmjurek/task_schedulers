import random

n = 0


def write_random(outFile):
    for i in range(n):
        p = random.randint(1, 15)
        r = random.randint(0, 100)
        d = random.randint(p + r, p + r + 200)
        w = random.randint(1, 10)
        outFile.write('{} {} {} {}\n'.format(p, r, d, w))


if __name__ == '__main__':
    print("Started generator")
    count = 0

    for i in range(10):
        n += 50
        outFile = open("instances/132244-instance-{}.txt".format(n), "w")
        outFile.write(str(n) + '\n')
        write_random(outFile)
        outFile.close()
        count += 1
    print("Finished generating 10 instances")
