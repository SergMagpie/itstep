from pprint import pprint

graph = {
    "a": ["f", "c", "b"],
    "b": ["a", "c", "d"],
    "c": ['a', 'f', 'b', 'd'],
    "f": ['a', 'c', 'e'],
    "e": ["f", 'd'],
    "d": ["e", "c", "b"]
}


# class Vertex:
    
#     def __init__(self, data) -> None:
#         self.__data = data
    
#     def __str__(self) -> str:
#         return f"Vertex {self.data}"


class Graph:

    def __init__(self) -> None:
        self.__graph = {}

    def add_vertex(self, data):
        self.__graph[data] = []
    
    def add_connection(self, vertex1, vertex2, value):
        if vertex1 in self.__graph and vertex2 in self.__graph:
            if vertex2 not in [e[0] for e in self.__graph[vertex1]]:
                self.__graph[vertex1].append( (vertex2, value) )
                self.__graph[vertex2].append( (vertex1, value) )
                return True
        return False
    
    def __str__(self) -> str:
        return str(self.__graph)


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("c")
    g.add_vertex("b")

    g.add_connection("a", "c", 20)
    g.add_connection("a", "b", 24)
    g.add_connection("c", "d", 5)

    print(g)