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
        g.add_edges_from(self._edges)
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
    
    def draw_graph(self) -> None:
        """
        Рисует граф.
        """
        pos = nx.spring_layout(self._graph)
        nx.draw_networkx(self._graph, pos)
        plt.show()
    
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
  
    def get_shortes_path_method_dijkstra(self, start: int, end: int):
        """
        Возвращает кратчайшие пути методом Дейкстры.
        """
        unvisited_nodes = list(self._graph.nodes)

        shortest_path = {}
    
        previous_nodes = {}
    
        max_value = float("inf")
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        
        shortest_path[start] = 0
        
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            neighbors = self._graph.neighbors(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + 1
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
    
            unvisited_nodes.remove(current_min_node)
        
        path = [start]
        node = end
        while node != start:
            path.append(node)
            node = previous_nodes[node]
        return sorted(path)
    