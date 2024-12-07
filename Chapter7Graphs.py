class Graph:
    __n = 0
    __g = [[0 for x in range(10)] for y in range(10)]

    def __init__(self, x):
        self.__n = x
        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__g[i][j] = 0

    def inputFunction(self):
        print("Enter the adjacency matrix:")
        for i in range(self.__n):
            for j in range(self.__n):
                self.__g[i][j] = int(input(f"Enter element at ({i}, {j}): "))

    def displayAdjacencyMatrix(self):
        print("\n Adjacency Matrix:", end="")

        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__g[i][j], end="")

    def removeVertex(self, x):
        if (x > self.__n):
            print("Vertex not present !")
        else:
            while (x < self.__n):
                for i in range(0, self.__n):
                    self.__g[i][x] = self.__g[i][x + 1]
                for i in range(0, self.__n):
                    self.__g[x][i] = self.__g[x + 1][i]
                x = x + 1
            self.__n = self.__n - 1

n = int(input("Enter a number of nodes to produce a Graph: "))
g = Graph(n)
g.inputFunction()

print("\nGraph before deletion:")
g.displayAdjacencyMatrix()

nodeDelete = int(input("\n\nEnter a node to delete: "))
g.removeVertex(nodeDelete)

print("\nGraph after deletion:")
g.displayAdjacencyMatrix()
