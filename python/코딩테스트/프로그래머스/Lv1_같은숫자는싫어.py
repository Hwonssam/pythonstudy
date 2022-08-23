def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if i != (len(arr) -1) and arr[i] != arr[i+1] :
            answer.append(arr[i])
    if answer ==[]:
        answer.append(arr[0])
    if arr[-1] != answer[-1] :
        answer.append(arr[-1])
    return answer

print(solution([4,4,4]))
