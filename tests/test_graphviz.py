import pygraphviz as pgv

from unittest import TestCase


class TestGraphviz(TestCase):

    def test_self_reference(self):
        G = pgv.AGraph()
        G.add_node('a')
        G.add_edge('a', 'a')
        print(G)
