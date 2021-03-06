import copy
import numpy as np
import unittest

from ugd.help_function.graph_creation import graph_to_adj_m, adj_m_to_graph
from ugd.help_function.util import get_path
from ugd.schlaufen_construction.di_schlaufen_construction_util import mark_edge
from test.test_resources.graphs_two_restriction_sets import graph1, graph1_adj_m


class HelpFunctionsAndUtil(unittest.TestCase):



    def test_adj_m_to_graph(self):
        adj_m = graph1_adj_m
        graph = adj_m_to_graph(adj_m, is_directed=True)
        adj_m_2 = graph_to_adj_m(graph)
        assert np.array_equal(adj_m_2 , adj_m)


    def test_graph_to_adj_m(self):
        graph = graph1
        adj_m = graph1_adj_m
        graph_copy = copy.deepcopy(graph)
        adj_m_verg = graph_to_adj_m(graph_copy)
        assert np.array_equal(adj_m_verg, adj_m)


    def test_get_path(self):
        pathgraph = copy.deepcopy(graph1)
        mark_edge(pathgraph, 3, 2, True, 1)
        mark_edge(pathgraph, 2, 1, False, 1)
        mark_edge(pathgraph, 1, 0, True, 1)
        mark_edge(pathgraph, 0, 3, False, 1)
        active_start = True

        path = get_path(3, active_start, pathgraph, 1)
        assert path == [3,2,1,0,3]