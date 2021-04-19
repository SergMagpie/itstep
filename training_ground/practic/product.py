class Product:
    def __init__(self, product_name, cost) -> None:
        self.product_name, self.cost = product_name, cost


class Basket:
    def __init__(self) -> None:
        self.roster = []

    def add_prod(self, product_name, cost):
        self.roster.append(Product(product_name, cost))

    def total_price(self):
        return sum([i.cost for i in self.roster])

    def total_quantity(self):
        return len(self.roster)

    def __iter__(self):
        return iter((i.product_name, i.cost) for i in self.roster)


    # def __next__(self):
        # 	return
if __name__ == "__main__":
    package = Basket()
    package.add_prod('Rice', 50)
    package.add_prod('Banana', 77)
    package.add_prod('Meat', 70)
    package.add_prod('Bread', 30)
    print(package.total_price())
    print(package.total_quantity())
    for i in package:
        print(i)
