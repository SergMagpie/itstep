def add_cost_2019(money):
    return money + 200


def add_cost_2020(money):
    return money + 150


def parent_function(child_function, a: int) -> int:
    result = child_function(a)
    return result + 10

print(parent_function(add_cost_2019, 2000))
print(parent_function(add_cost_2020, 2000))