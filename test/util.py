import sys

from rdflib import Graph
from rdflib.compare import isomorphic

from csv2graph.namespace import fdmontology, kompetenz, lernniveaustufe, zielgruppe
from csv2graph.settings import PREFIX_LO, PREFIX_CLUSTER, PREFIX_TOPIC


def same_graphs(g1: Graph, g2: Graph) -> bool:
    if isomorphic(g1, g2):
        return True

    print("Graphs do not match: ", file=sys.stderr)
    print(g1.serialize(), file=sys.stderr)
    print("------------", file=sys.stderr)
    print(g2.serialize(), file=sys.stderr)

    return False


_NAMESPACE_PREFIXES = {
    "o": fdmontology.NS,
    "komp": kompetenz.NS,
    "lns": lernniveaustufe.NS,
    "zg": zielgruppe.NS,
    "lz": PREFIX_LO,
    "tc": PREFIX_CLUSTER,
    "thema": PREFIX_TOPIC,
}


def graph() -> Graph:
    g = Graph()
    for prefix, namespace in _NAMESPACE_PREFIXES.items():
        g.bind(prefix, namespace)
    return g
