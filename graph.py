#Graph Implementation (undirected graph)

class Graph:
    def __init__(self) -> None:
        self.number_of_vertices = 0 
        self.adjacent_list = {}

    def add_vertex(self,vertex):
        self.number_of_vertices+=1
        self.adjacent_list[str(vertex)] = []
    
    def add_edge(self,vertex1,vertex2):
        if not all(key in self.adjacent_list for key in (str(vertex1), str(vertex2))):
            return "Error"
        else:
            #undirected graph
            self.adjacent_list[str(vertex1)].append(str(vertex2))
            self.adjacent_list[str(vertex2)].append(str(vertex1))

    def __str__(self) -> str:
        s=""
        for vertex in self.adjacent_list.keys():
            s+= str(vertex) + "--> " + str(self.adjacent_list[str(vertex)]) + "\n"
        return s


def main():
    g=Graph()
    for i in range(7):
        g.add_vertex(i)
    print(g)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,2)
    g.add_edge(4,3)
    g.add_edge(4,2)
    g.add_edge(4,5)
    g.add_edge(6,5)
    print(g)

if __name__ == "__main__":
    main()