def solution(sizes):
    xs=[]
    ys=[]
    for i in range(len(sizes)):
        a = sizes[i][0]
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = a
        xs.append(sizes[i][0])
        ys.append(sizes[i][1])
    answer = max(xs)*max(ys)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))