k, n = map(int, input().split())

page = (n // k) + (n % k > 0)
line = n - ((page - 1) * k)
print(page, line)
