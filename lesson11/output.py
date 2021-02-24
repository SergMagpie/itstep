from pprint import pprint

biggest_cities = ["Tokyo", "Delhi", "Shanghay", "Mexico City", "Sap Paulo",
                  "Mumbai", "Kinki maior metropolian area", "Cairo"]

pairs = zip(biggest_cities, range(1, 9))
# pairs = [(i, j + 1) for j, i in enumerate(biggest_cities)]

pprint(list(pairs))
