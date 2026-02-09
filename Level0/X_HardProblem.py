A, B, C = map(int, input().split())

ls = [A, B, C]
ma = max(ls)
mi = min(ls)

mid = (A+B+C) - ma - mi

print(f'{mi} {mid} {ma}')