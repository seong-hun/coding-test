import sys
import math

n, m, *nums = map(int, sys.stdin.read().rstrip().split())
counter = [0] * m
counter[s := 0] = 1
for num in nums:
    counter[s := (s + num) % m] += 1
print(sum(math.comb(i, 2) for i in counter))
