def solution(n):
    answer = 0
    li = list(str(n))

    for i in range(0,len(li)):
        answer += int(li[i])

    return answer

s = input("자릿수 더하기 숫자를 입력하세요.")

print(str(s)+"의 모든 자릿수 합은"+str(solution(s))+"입니다.")