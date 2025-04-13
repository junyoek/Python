# a = 12345
# answer = list(str(a))
# print(answer)

# li = answer[::-1]


# print(li)

def solution(n):
    answer = []

    li = list(n)
    answer  = li[::-1]

    return answer

user_input = input("자연수를 입력하세요.")

print(solution(user_input))

