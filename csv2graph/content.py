from typing import Dict

from rdflib import Graph, RDF, SKOS
from rdflib.term import Node, BNode, Literal

from csv2graph.namespace import fdmontology


def add_content(g: Graph, definitions_dict: Dict) -> Node:
    content_node = BNode()
    g.add((content_node, RDF.type, fdmontology.Inhalt))
    for lang, definition in definitions_dict.items():
        g.add((content_node, SKOS.definition, Literal(definition, lang=lang)))

    return content_node
