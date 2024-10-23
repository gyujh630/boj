import sys

fst = sys.stdin.readline().rstrip()
sec = sys.stdin.readline().rstrip()
thd = sys.stdin.readline().rstrip()

a = [0, fst, sec, thd]

for i in range(1, len(a)):
    if str.isdigit(a[i]):
        next_num = int(a[i]) + 4 - i

        s = ''
        if next_num % 3 == 0:
            s += 'Fizz'
        if next_num % 5 == 0:
            s += 'Buzz'
        if s != '':
            print(s)
        else:
            print(next_num)
        break