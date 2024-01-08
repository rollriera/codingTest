import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))

a_sum = a[0]

l = 0
r = 1

count = 0

while True:
    if a_sum < m:
        if r < n:
            a_sum += a[r]
            r += 1
        else:
            break
    elif a_sum == m:
        count += 1
        a_sum -= a[l]
        l += 1  
    else: 
        a_sum -= a[l]
        l += 1    

print(count)        