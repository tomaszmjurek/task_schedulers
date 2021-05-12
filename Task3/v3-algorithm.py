import sys
from operator import add
from statistics import mean


# od razu dodany indeks
def read_instance_file(f):
    n = int(f.readline())
    p1, p2, p3, d, w = [], [], [], [], []
    lines = []
    for i in range(n):
        tail = [int(x) for x in f.readline().split()]
        tail.append(i + 1)
        p1.append(tail[0])
        p2.append(tail[1])
        p3.append(tail[2])
        d.append(tail[3])
        w.append(tail[4])
        lines.append(tail)
    return n, lines, p1, p2, p3, d, w


def choose_shortest(p1, p2, p3):
    p1_min = min(p1)
    p2_min = min(p2)
    p3_min = min(p3)

    if p1_min <= p2_min:
        if p1_min <= p3_min:
            return p1, p2, p3
        else:
            return p3, p2, p2
    if p2_min <= p3_min:
        return p1, p3, p2
    else:
        return p1, p2, p3


def jureks_algorithm(p1, p2, p3, d, w):
    # KROK 1. Wyznaczenie najszybszej z 3 linii
    a, b, c = choose_shortest(p1, p2, p3)

    # KROK 2. Agregacja do 2 linii
    P1 = list(map(add, a, b))
    P2 = list(map(add, b, c))

    # KROK 3. Podział zadań na dwie grupy
    G1 = []
    G2 = []
    for i in range(len(P1)):
        p1 = P1[i]
        p2 = P2[i]
        w_i = w[i]
        d_i = d[i]
        if p1 <= p2:
            G1.append([p1, p2, i+1, d_i, w_i])
        else:
            G2.append([p1, p2, i+1, d_i, w_i])

    # KROK 4. Sortowanie grup z uwzględnieniem p, d, w
    G1.sort(key=lambda x: x[0] + x[3] - x[4])
    G2.sort(key=lambda x: x[1] + x[3] - x[4]) #G2.sort(key=lambda x: x[1] - x[3] + x[4], reverse=True)

    # KROK 5. Uszeregowanie zadań
    G = G1 + G2
    print(G)
    result = [task[2] for task in G]
    return result


def check(instances, solutions):
    D = 0.00
    W = 0
    time_m1, time_m2, time_m3 = 0, 0, 0
    for t in solutions:
        p1, p2, p3, d, w, null = instances[t - 1]
        time_m1 += p1
        time_m2 = max(time_m1, time_m2) + p2
        time_m3 = max(time_m2, time_m3) + p3
        Dj = max(0, time_m3 - d)
        D += (w * Dj)
        W += w
    D = D / W
    D = round(D, 2)
    return D


def save_solution(n, D, result):
    outFile = open("132244-solution-{}.txt".format(n), "w")
    outFile.write(str(D) + '\n')
    for index in result:
        outFile.write(str(index) + " ")
    outFile.write('\n')
    outFile.close()


if __name__ == '__main__':
    try:
        inFile = sys.argv[1]
        file = open(inFile, "r")
    except:
        print('Problem with opening file: no argument or no file. Quitting...')
        exit()

    n, tasks, p1, p2, p3, d, w = read_instance_file(file)
    # print(f'n = {n}')
    # print(f'instances = {tasks}')

    res = jureks_algorithm(p1, p2, p3, d, w)
    # print(f'result = {res}')
    D = check(tasks, res)
    print(f'D = {D}')
    save_solution(n, D, res)