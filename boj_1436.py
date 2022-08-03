import sys

n = int(sys.stdin.readline())
num = 666
count = 0

while count <= 10000:
    if '666' in str(num):
        count += 1
    if count == n:
        print(num)
        break
    num += 1


