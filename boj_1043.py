import sys

N, M = map(int, sys.stdin.readline().split())

d_input = list(map(int, sys.stdin.readline().split()))
danger = set(d_input[1:])

parties = []

for m in range(M):
    p_input = list(map(int, sys.stdin.readline().split()))
    parties.append(p_input[1:])

while True:
    remove_list = []
    for i in range(len(parties)):
        for j in range(len(parties[i])):
            if parties[i][j] in danger:
                remove_list.append(i)

    if len(remove_list) == 0:
        break
    new = []
    for i in range(len(parties)):
        if i not in remove_list:
            new.append(parties[i])
        else:
            danger = set(list(danger) + parties[i])

    parties = new

print(len(parties))