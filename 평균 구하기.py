def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum += int(i)

    answer = sum/len(arr)

    return answer

li = [1,2,3,4,5]

print(solution(li))