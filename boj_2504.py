# 2504번: 괄호의 값

import sys

str = sys.stdin.readline().rstrip()


def main():
    stack = []
    temp = 1
    answer = 0

    for i in range(len(str)):
        if str[i] == '(':
            temp *= 2
            stack.append(str[i])
        elif str[i] == '[':
            temp *= 3
            stack.append(str[i])
        elif str[i] == ')':
            if not stack or stack[-1] == '[':
                return 0
            if str[i-1] == '(':
                answer += temp
            stack.pop()
            temp //= 2
        else: # str[i] == ']'
            if not stack or stack[-1] == '(':
                return 0
            if str[i - 1] == '[':
                answer += temp
            stack.pop()
            temp //= 3
    if stack:
        return 0
    return answer


print(main())
