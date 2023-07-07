import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

count = [0] * M
count[(sum := 0)] = 1

for a in A:
    count[(sum := (sum + a) % M)] += 1

sum = 0
for c in count:
    sum += c * (c-1)/2

print(int(sum))

