import sys


def calculate_minimum_changes(matrix, n, m):
    mini = float('inf')
    for i in range(n - 7):  # y축 시작점
        for j in range(m - 7):  # x축 시작점
            count_b_start = 0
            count_w_start = 0

            for x in range(8):
                for y in range(8):
                    expected_char_b = 'B' if (x + y) % 2 == 0 else 'W'
                    expected_char_w = 'W' if (x + y) % 2 == 0 else 'B'
                    actual_char = matrix[i + x][j + y]

                    if actual_char != expected_char_b:
                        count_b_start += 1
                    if actual_char != expected_char_w:
                        count_w_start += 1

            # 최소 변경 횟수 업데이트
            mini = min(mini, count_b_start, count_w_start)
    return mini


n, m = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().strip() for _ in range(n)]

# matrix에서 count 계산
original_minimum = calculate_minimum_changes(matrix, n, m)

print(original_minimum)
