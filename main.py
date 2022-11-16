import Graphs
import pandas

if __name__ == "__main__":
    n = int(input("Введите количество вершин: "))
    e = int(input("Введите количество ребер: "))
    graph = Graphs.Graphs(n, e)
    print("Матрица ицидентности => \n", pandas.DataFrame(graph.get_incidence_matrix()))
    print("Матрица смежности: => \n", pandas.DataFrame(graph.get_adjacency_matrix()))
    if input("Показать кратчайщие пути? (y/n): ") == "y":
        start = int(input("Введите начальную вершину: "))
        end = int(input("Введите конечную вершину: "))
        print("Кратчайшие пути => \n", pandas.DataFrame(graph.get_shortest_paths(start, end)))
    graph.draw_graph()