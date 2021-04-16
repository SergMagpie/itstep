l = ['Arabica',
     'Robusta',
     'Liberica',
     'Excelsa',
     'Typica',
     'Kona',
     'Java',
     'Jamaican Blue Mountain',
     'Sumatra',
     'Bergendal',
     'Rume Sudan',
     'Amarello de Botancatú',
     'Blawan Paumah',
     'Java Mocha',
     'Pluma Hidalgo',
     'Creole',
     'Ethiopian Harrar',
     'Blue Mountain',
     'Villa Sarchi',
     'Ethiopian Sidamo',
     'Ethiopian Yiragacheffe',
     'San Ramón',
     'Sidikalang']
d = dict(enumerate(l))
print("\n".join("'{}' - {}".format(k, v) for k, v in d.items()))
a = [i for i in d][1]
print(type(a))