auto_makers_cort = ('Volkswagen AG',
               'Toyota Motor',
               'Renault-Nissan-Mitsubishi Alliance',
               'Hyundai-Kia',
               'General Motors',
               'Ford Motor',
               'Honda Motor',
               'Suzuki')
auto_makers = list(auto_makers_cort)
print(*auto_makers_cort, sep=', ')
maker = input("Enter auto maker's mame ")
changer = input("Enter name for change ")
for i, j in enumerate(auto_makers):
    if j == maker:
        auto_makers[i] = changer
auto_makers_cort =   tuple(auto_makers)   
print(*auto_makers_cort, sep=', ')
