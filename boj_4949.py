#4949번: 균형잡힌 세상

import sys

def test(s):
    stack = []
    for i in range(len(s)):
        char = s[len(s)-2-i]    #문자열의 뒷부분부터 탐색, -2를 하면 마지막 '.'을 생략 가능

        if char == ']':
            stack.append(']')
        elif char == ')':
            stack.append(')')
        elif char == '[':
            if len(stack) == 0: #스택이 비어있는데 왼쪽 괄호가 들어온 경우
                return 'no'
            else:
                if stack[len(stack)-1] != ']': #같은 종류 괄호끼리 짝지어지지 않은 경우
                    return 'no'
                else: stack.pop()
        elif char == '(':
            if len(stack) == 0: #스택이 비어있는데 왼쪽 괄호가 들어온 경우
                return 'no'
            else:
                if stack[len(stack)-1] != ')': #같은 종류 괄호끼리 짝지어지지 않은 경우
                    return 'no'
                else: stack.pop()
    if len(stack) == 0:  #스택이 비어있다면 (오른쪽괄호 수 = 왼쪽괄호 수)
        return 'yes'
    else: return 'no'    #비어있지 않음 (오른쪽괄호 수 > 왼쪽괄호 수)

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':        #'.' 하나만 있는 경우 (입력종료조건)
        break
    print(test(s))