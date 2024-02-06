from typing import Dict

from rdflib import Graph, URIRef, SKOS
from rdflib.term import Node, Literal

from csv2graph.settings import PREFIX_LO, HEADER_LO_ID, LO_HEADER_LANGUAGE_ASSOCIATION


def _add_definitions_to_learning_objective(g: Graph, lo_node: Node, row: Dict):
    for lang, header in LO_HEADER_LANGUAGE_ASSOCIATION.items():
        g.add((lo_node, SKOS.definition, Literal(row[header], lang=lang)))


def add_learning_objective(g: Graph, row: Dict):
    lo_node = URIRef(PREFIX_LO + row[HEADER_LO_ID])

    _add_definitions_to_learning_objective(g, lo_node, row)
