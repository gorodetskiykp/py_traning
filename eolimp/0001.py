""" https://www.eolymp.com/ru/contests/26627/problems/305403"""
from math import factorial as f


def binom(n, k):
    return int(f(n) / (f(k) * f(n - k)))


result = []

for _ in range(int(input())):
    n, k = input().split()
    result.append(binom(int(n), int(k)))

# for n in range(10):
#     for k in range(10):
#         if 0 <= k <= n:
#             print(n, k, binom(n, k))

print(*result, sep='\n')
