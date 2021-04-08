class Counter():

    counter = 0

    def __call__(self):
        self.counter += 1
        print(self.counter)

def sum10():
    x = 10
    def inner(*args):
        return x + args[0]  
    return inner     

if __name__ == "__main__":
    s = Counter()
    s()
    s()
    s = sum10()
    res = s(5)
    print(res)
    print(sum10()(5))