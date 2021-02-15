s = [[], [], []]
[s[(i == 0) + (i > 0) + (i > 0)].append(i) for i in [int(input()) for _ in range(int(input()))]]
print(*[el for lst in s for el in lst], sep='\n')
