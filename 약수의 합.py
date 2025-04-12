def s(n):
    n = int(n)
    n_list = []

    for i in range(1,n+1):
        if(n%i == 0):
            n_list.append(i)
    
    total = 0
    for k in range(0,len(n_list)):
        total += n_list[k]

    answer = total
    return(answer)

i = input()

print("입력한",str(i), "의 약수의 합은",str(s(i)),"입니다.")