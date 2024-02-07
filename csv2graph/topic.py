from typing import Dict

from rdflib import Graph, RDFS, RDF
from rdflib.term import Node, URIRef, Literal

from csv2graph.namespace import fdmontology
from csv2graph.settings import PREFIX_TOPIC


def add_topic(g: Graph, cluster_id: str, topic_id: str, labels_dict: Dict) -> Node:
    if not cluster_id:
        raise Exception("Missing cluster id")
    if not topic_id:
        raise Exception("Missing topic id")

    topic_node = URIRef(PREFIX_TOPIC + f"{cluster_id}-{topic_id}")
    g.add((topic_node, RDF.type, fdmontology.Thema))
    for lang, label in labels_dict.items():
        g.add((topic_node, RDFS.label, Literal(label, lang=lang)))

    return topic_node
