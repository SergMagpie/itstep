def triple_result(funk):
    def wrapper(*args):
        return funk(*args) * 3
    return wrapper


@triple_result
def add(a: int, b: int) -> int:
    return a + b


print(add(5, 5))
