import sys
n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

three = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
            continue
        for k in range(len(a)):
            if a[i] == a[j] or a[j] == a[k] or a[i] == a[k]:
                continue
            if a[i] + a[j] + a[k] <= m:
                three.append(a[i] + a[j] + a[k])

print(max(three))

"""
좋은 풀이

def main():
    max_sum = 0
    N, M = map(int, input().split())
    nums_list = list(map(int, input().split()))
    for i in range(len(nums_list)-2):
        for j in range(i+1, len(nums_list)-1):
            for k in range(j+1, len(nums_list)):
                tot = nums_list[i] + nums_list[j] + nums_list[k]
                if tot > max_sum and tot <= M:
                    max_sum = tot
    print(max_sum)
    
if __name__ == "__main__":
    main()
"""