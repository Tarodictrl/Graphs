import Graphs
import pandas

if __name__ == "__main__":
    n = int(input("Введите количество вершин: "))
    e = int(input("Введите количество ребер: "))
    graph = Graphs.Graphs(n, e)
    print("Матрица ицидентности => \n", pandas.DataFrame(graph.get_incidence_matrix()))
    print("Матрица смежности: => \n", pandas.DataFrame(graph.get_adjacency_matrix()))
    if input("Показать кратчайщие пути? (y/n): ") == "y":
        start = int(input(f"Введите начальную вершину от 1 до {n}: "))
        end = int(input(f"Введите конечную вершину от 1 до {n}: "))
        length = int(input("Введите длину пути: "))
        print("Кратчайшие пути => \n", graph.get_shortes_path_method_dijkstra(start, end))
    graph.draw_graph()