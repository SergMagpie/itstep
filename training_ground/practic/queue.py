

class Queue:

    def __init__(self) -> None:
        self.__queue = []
    

    def add(self, data):
        self.__queue.append(data)
    
    def pop(self):
        if self.__queue:
            return self.__queue.pop(0)
        return None
    
    def __str__(self) -> str:
        return str(self.__queue)


if __name__ == "__main__":
    queue = Queue()

    queue.add("google")
    queue.add("wikipedia")
    queue.add("wikipedia Ukraine")

    print(queue)

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

    print(queue)
    queue.add("asdas")
    print(queue)