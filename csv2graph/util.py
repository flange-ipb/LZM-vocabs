from rdflib import Graph

from csv2graph.namespace import fdmontology, kompetenz, lernniveaustufe, zielgruppe
from csv2graph.settings import PREFIX_LO, PREFIX_CLUSTER, PREFIX_TOPIC

_NAMESPACE_PREFIXES = {
    "komp": kompetenz.NS,
    "lns": lernniveaustufe.NS,
    "lz": PREFIX_LO,
    "o": fdmontology.NS,
    "tc": PREFIX_CLUSTER,
    "thema": PREFIX_TOPIC,
    "zg": zielgruppe.NS,
}


def graph() -> Graph:
    g = Graph()
    for prefix, namespace in _NAMESPACE_PREFIXES.items():
        g.bind(prefix, namespace)
    return g
