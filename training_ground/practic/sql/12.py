# яжпрограмист, яжнебуду руками все это набирать ;)
menu = (
        'Display of all transactions',
        'Display of all sellers',
        'Display of all buyers',
        'Display of transactions of a specific seller',
        'Display of the maximum transaction amount',
        'Display of the minimum transaction amount',
        'Display the maximum transaction amount for specific seller',
        'Display the minimum transaction amount for specific seller',
        'Display the maximum transaction amount for specific buyer',
        'Display the minimum transaction amount for specific buyer',
        'Display the seller who has the maximum the amount of sales for all transactions',
        'Display of the buyer who has the maximum the amount of purchases on all transactions',
    )

for n, i in enumerate(menu):
    string = ''
    for j in i:
        if j == ' ':
            string += '_'
        else:
            string += j.lower()
    print(f"'{n + 1}': ('{n + 1} - {i}',\n\t{string}),")
    # print(f"def {string}():\n\tpass")
