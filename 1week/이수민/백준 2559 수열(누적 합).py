import sys

input = sys.stdin.readline

# n = 배열길이 k = 계산할 날짜의 수
n, k = map(int, input().split())

# 배열 초기화
a = list(map(int, input().split()))

# 최대값을 구할 배열
result = []

# 배열에 먼저 첫번쨰 합을 초기화
result.append(sum(a[:k]))

# 배열의 길이 - 계산할 날짜의 수 = 총 계산할 횟수
for i in range(n - k):
  
  # 첫번째 합 - 입력받은 수[첫번째] - 입력받은 수[i + 계산할 위치]
  # 첫번째 수를 계산한 후 다음 계산할 위치까지 더해준 후에 기존에 계산한 값을 빼주어야함
  result.append(result[i] - a[i] + a[i+k])

print(max(result)) 

