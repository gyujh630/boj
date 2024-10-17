def solution(scores):
    wh = scores[0]
    sum_wh = wh[0] + wh[1]

    scores.sort(key=lambda x: (-x[0], x[1]))  # 근무태도 내림차순, 동료평가 오름차순
    top_score = scores[0]
    answer = 1

    for i in range(len(scores)):
        if wh[0] < top_score[0] and wh[1] < top_score[1]:
            return -1

        if scores[i][1] >= top_score[1]:  # 동료평가 비교. top 동료평가보다 작은 경우를 배제(인센티브 못받는사람)
            if sum(scores[i]) > sum(wh):
                answer += 1
            top_score = scores[i]

    return answer