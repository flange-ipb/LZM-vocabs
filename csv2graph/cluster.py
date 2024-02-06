from typing import Dict

from rdflib import Graph, RDFS
from rdflib.term import Node, URIRef, Literal

from csv2graph.settings import PREFIX_CLUSTER


def add_cluster(g: Graph, cluster_id: str, names_dict: Dict) -> Node:
    if not cluster_id:
        return

    cluster_node = URIRef(PREFIX_CLUSTER + cluster_id)
    for lang, label in names_dict.items():
        g.add((cluster_node, RDFS.label, Literal(label, lang=lang)))

    return cluster_node
