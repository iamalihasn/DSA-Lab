num = [2,3,2]
k = 2
time = 0
for i in range(len(num)):
    if i <= k:
        time += min(num[k],num[i])
    else:
        time += min(num[k]-1,num[i])

print(time)