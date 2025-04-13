def solution(num):
    answer = ''

    if num%2 == 0 or num ==0:
        answer = "Even"
    else:
        answer = "Odd"


    return answer

user_input = int(input("자연수를 입력하세요."))

print(solution(user_input))

