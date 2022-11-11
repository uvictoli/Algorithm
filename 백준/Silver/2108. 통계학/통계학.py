import sys
from collections import Counter
#statistics의 mode는 최빈값이 여러 개일 때 가장 작은 수 출력

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    
nums.sort()

avg = round(sum(nums) / n)
# if abs(avg) == 0:   avg = 0
print(avg)


mid = n // 2 
print(nums[mid])

if n > 1:
    cnt = Counter(nums)
    modes = cnt.most_common(2) #list
    if modes[0][1] == modes[1][1]:  
        print(modes[1][0])
    else:   
        print(modes[0][0])
else:
    print(nums[0])

ran = nums[-1] - nums[0]
print(ran)