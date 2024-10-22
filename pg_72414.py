def convertSec(str):
    h, m, s = map(int, str.split(':'))
    return h * 3600 + m * 60 + s


def convertLogToSec(log_str):
    start, end = log_str.split('-')
    return convertSec(start), convertSec(end)


def convertStr(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02}:{m:02}:{s:02}"


def solution(play_time, adv_time, logs):
    play_time = convertSec(play_time)
    adv_time = convertSec(adv_time)

    timeline = [0] * (play_time + 1)

    for log in logs:
        start, end = convertLogToSec(log)
        timeline[start] += 1
        timeline[end] -= 1

    for i in range(1, play_time):  # 구간별 현재 시청자 수 계산
        timeline[i] += timeline[i - 1]

    for i in range(1, play_time):  # 구간별 누적 시청자 수 계산
        timeline[i] += timeline[i - 1]

    max_time = 0
    best_start = 0

    for i in range(play_time - adv_time + 1):
        cur_time = timeline[i + adv_time - 1] - timeline[i - 1]
        if cur_time > max_time:
            max_time = cur_time
            best_start = i

    return convertStr(best_start)