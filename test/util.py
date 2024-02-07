import sys

from rdflib import Graph
from rdflib.compare import isomorphic


def same_graphs(g1: Graph, g2: Graph) -> bool:
    if isomorphic(g1, g2):
        return True

    print("Graphs do not match: ", file=sys.stderr)
    print(g1.serialize(), file=sys.stderr)
    print("------------", file=sys.stderr)
    print(g2.serialize(), file=sys.stderr)

    return False
