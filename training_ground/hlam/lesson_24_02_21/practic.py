# task 1
print(list(map(lambda x: x ** 2 if 10 <= x <=
               20 else None, [0, 3, 5, 10, 15, 20, 25])))

# task 2
s = ['ghsdgdf', 'fdsa', 'dagagr']
s1 = list(filter(lambda x: len(x) > 6, s))
print(s1)

# task 3
n = [0, 3, 5, 10, 15, 20, 25]
n1 = list(map(lambda x: x ** 2 if 10 <= x <= 20 else None, n))
print(n1)
n2 = [x ** 2 for x in n if 10 <= x <= 20]
print(n2)

# task 4
text = ['ghsdgdf', 'fdsa', 'Dagagr']
text1 = list(filter(lambda x: x[0].isupper(), text))
print(text1)

# task 5
text = ['ghsdgdf', 'fdsa', 'Dagagr']
text1 = list(map(lambda x: x.upper(), text))
print(text1)
