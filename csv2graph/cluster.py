from typing import Dict

from rdflib import Graph, RDFS, RDF
from rdflib.term import Node, URIRef, Literal

from csv2graph.namespace import fdmontology
from csv2graph.settings import PREFIX_CLUSTER


def add_cluster(g: Graph, cluster_id: str, labels_dict: Dict) -> Node:
    if not cluster_id:
        raise Exception("Missing cluster id")

    cluster_node = URIRef(PREFIX_CLUSTER + cluster_id)
    g.add((cluster_node, RDF.type, fdmontology.Themenbereich))
    for lang, label in labels_dict.items():
        g.add((cluster_node, RDFS.label, Literal(label, lang=lang)))

    return cluster_node
