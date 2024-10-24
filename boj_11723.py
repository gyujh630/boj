import sys


M = int(sys.stdin.readline())
S = set()
for m in range(M):
    command = sys.stdin.readline().rstrip()
    if command == "all" or command == "empty":
        if command == "all":
            S = set([i for i in range(1,21)])
        elif command == "empty":
            S = set()

    else:
        c_list = command.split()
        command, num = c_list[0], c_list[1]
        num = int(num)
        if command == "add":
            S.add(num)
        elif command == "remove":
            if num in S:
                S.remove(num)
        elif command == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)

