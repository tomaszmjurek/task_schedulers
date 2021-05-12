import random
from sys import argv


def write_random(n, outFile):
    for i in range(n):
        p1 = random.randint(5, 15)
        p2 = random.randint(15, 25)
        p3 = random.randint(20, 35)
        min_p = p1 + p2 + p3
        d = random.randint(min_p + n, n * min_p)
        w = random.randint(1, 10)
        outFile.write('{} {} {} {} {}\n'.format(p1,p2,p3,d,w))


if __name__ == '__main__':
    n = int(argv[1])

    outFile = open(f"132244-instance-{n}.txt", "w")
    outFile.write(str(n) + '\n')
    write_random(n, outFile)
    outFile.close()
    print(f'Finished generating instance with n = {n}')