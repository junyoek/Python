def solution(x, n):
    answer = []

    for i in range(n):
        answer.append(x * (i + 1))

    return answer

first_input = -4
second_input = 2

print(solution(first_input, second_input))