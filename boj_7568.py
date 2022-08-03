import sys

n = int(sys.stdin.readline())
people = []
for i in range(n):
    tall, weight = map(int, sys.stdin.readline().split())
    people.append([tall, weight])

for i in range(len(people)):
    count = 0
    for j in range(len(people)):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]: #키 몸무게 둘다 큰지 검사
            count += 1                      #덩치가 더 큰 사람 카운트 + 1
    print(count + 1, end = ' ')
