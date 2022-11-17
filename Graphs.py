import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class Graphs:
    def __init__(self, n: int, e: int) -> None:
        """
        n - количество вершин.
        e - количество ребер.
        """
        self._number_of_vertices: int = n
        self._number_of_edges: int = e
        self._vertices: set = self._generate_vertices()
        self._edges: list = self._generate_edges()
        self._incidence_matrix: np.ndarray = self._generate_matrix_incidence()
        self._graph: nx.Graph = self._generate_graph()

    def _generate_graph(self) -> nx.Graph:
        """
        Генерирует граф.
        """
        g = nx.Graph()
        g.add_nodes_from(self._vertices)
        for edge in self._edges:
            g.add_edge(edge[0], edge[1], weight=random.randint(1, 10))
        g.add_edges_from(self._edges)
        return g

    def _generate_vertices(self) -> set:
        """
        Генерирует вершины.
        """
        return set([i+1 for i in range(self._number_of_vertices)])
    
    def _generate_edges(self) -> list:
        """
        Генерирует ребра.
        """
        array: list = [] 
        for i in range(self._number_of_edges):
            edge = (random.randint(0, self._number_of_vertices - 1), random.randint(0, self._number_of_vertices - 1))
            array.append(edge)
        return array

    def draw_graph(self) -> None:
        """
        Рисует граф.
        """
        pos = nx.spring_layout(self._graph)
        nx.draw_networkx(self._graph,pos)
        labels = nx.get_edge_attributes(self._graph,'weight')
        nx.draw_networkx_edge_labels(self._graph, pos, edge_labels=labels)
        plt.show()
    
    def _generate_matrix_incidence(self) -> np.ndarray:
        """
        Генерирует матрицу инцидентности.
        """
        incidence_matrix = np.zeros([max(self._vertices) + 1, len(self._edges)], dtype="int")
        for i, edge in enumerate(self._edges):
            l, r = edge
            incidence_matrix[l][i] = 1
            incidence_matrix[r][i] = 1
        return incidence_matrix
    
    def get_incidence_matrix(self) -> np.ndarray:
        """
        Возвращает матрицу инцидентности.
        """
        return self._incidence_matrix
   
    def get_adjacency_matrix(self) -> np.ndarray:
        """
        Возвращает матрицу смежности.
        """
        return nx.adjacency_matrix(self._graph).todense()

    def get_shortest_paths(self, start: int, end: int) -> list:
        """
        Возвращает кратчайшие пути.
        """
        # TODO: Сделать свой алгоритм поиска кратчайших путей методом Дейкстры.
        
        try:
            return nx.all_shortest_paths(self._graph, start, end, method="dijkstra")
        except Exception as e:
            print(e)
            return []
