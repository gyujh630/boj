#1874번: 스택 수열

def test(nums):
    stack = []
    count = 1
    print_list = []

    for num in nums:
        while num >= count:
            stack.append(count)
            print_list.append('+')
            count += 1
        if stack.pop() != num:     #stack.pop()이 실행됨과 동시에 num과 같은지 판단하는 것
            return 'NO'
        else:                      #stack.pop() == num이라면
            print_list.append('-')
    return '\n'.join(print_list)

import sys
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
print(test(nums))
