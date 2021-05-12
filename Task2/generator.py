import random
from sys import argv


def write_random(n, outFile):
    best = random.randint(0, 4)
    for i in range(5):
        if i == best:
            b = 1
        else:
            b = round(random.uniform(1, 3), 2)
        outFile.write(str(b) + ' ')

    outFile.write('\n')
    for i in range(n):
        p, r = random.randint(5, n * 2), random.randint(0, n * 30)
        outFile.write('{} {}\n'.format(p, r))


if __name__ == '__main__':
    n = int(argv[1])

    outFile = open(f"132244-instance-{n}.txt", "w")
    outFile.write(str(n) + '\n')
    write_random(n, outFile)
    outFile.close()
    print(f'Finished generating instance with n = {n}')

