from typing import Dict

from rdflib import Graph, RDFS
from rdflib.term import Node, URIRef, Literal

from csv2graph.settings import PREFIX_TOPIC


def add_topic(g: Graph, cluster_id: str, topic_id: str, names_dict: Dict) -> Node | None:
    if not cluster_id or not topic_id:
        return

    topic_node = URIRef(PREFIX_TOPIC + f"{cluster_id}-{topic_id}")
    for lang, label in names_dict.items():
        g.add((topic_node, RDFS.label, Literal(label, lang=lang)))

    return topic_node
