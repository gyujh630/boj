#재귀함수가 뭔가요?
#17478
import sys

def what(t):
    line = "____"
    if t >= 1:
       print(line*(n-t) + '"재귀함수가 뭔가요?"')
       print(line*(n-t) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
       print(line*(n-t) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
       print(line*(n-t) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
       what(t- 1)
    if t == 0:
        print(line*(n-t) + '"재귀함수가 뭔가요?"')
        print(line*(n-t) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    print(line*(n-t) + "라고 답변하였지.")

n = int(sys.stdin.readline())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
what(n)