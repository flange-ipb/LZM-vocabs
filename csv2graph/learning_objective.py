from typing import Dict

from rdflib import Graph, URIRef, SKOS, RDF
from rdflib.term import Node, Literal, BNode

from csv2graph.namespace import fdmontology
from csv2graph.settings import PREFIX_LO, HEADER_LO_ID, LO_HEADER_LANGUAGE_ASSOCIATION, HEADER_COMPETENCY_ASSOCIATION, \
    LEARNING_LEVELS_ASSOCIATION, HEADER_QUALIFICATION_LEVELS_ASSOCIATION


def _add_definitions(g: Graph, lo_node: Node, row: Dict):
    for lang, header in LO_HEADER_LANGUAGE_ASSOCIATION.items():
        g.add((lo_node, SKOS.definition, Literal(row[header], lang=lang)))


def _add_competency_level_to_learning_objective(g: Graph, lo_node: Node, competency: Node, learning_level: Node):
    cl_node = BNode()
    g.add((lo_node, fdmontology.fördertKompetenzstufe, cl_node))
    g.add((cl_node, RDF.type, fdmontology.Kompetenzstufe))

    g.add((cl_node, fdmontology.weistKompetenzZu, competency))
    #g.add((competency, fdmontology.wirdZuKompetenzstufeZugewiesen, cl_node))

    g.add((cl_node, fdmontology.weistLernniveaustufeZu, learning_level))
    #g.add((learning_level, fdmontology.wirdZuKompetenzstufeZugewiesen2, cl_node))


def _add_competency_levels(g: Graph, lo_node: Node, row: Dict):
    for header, competency in HEADER_COMPETENCY_ASSOCIATION.items():
        if learning_level := row[header]:
            _add_competency_level_to_learning_objective(g, lo_node, competency,
                                                        LEARNING_LEVELS_ASSOCIATION[learning_level])


def _add_qualification_level_to_learning_objective(g: Graph, lo_node: Node, level_node: Node):
    g.add((lo_node, fdmontology.istAbgestimmtAufZielgruppe, level_node))
    g.add((level_node, fdmontology.istZielgruppeVonLernziel, lo_node))


def _add_qualification_levels(g: Graph, lo_node: Node, row: Dict):
    for header, level in HEADER_QUALIFICATION_LEVELS_ASSOCIATION.items():
        has_level = row[header]
        if has_level == "X":
            _add_qualification_level_to_learning_objective(g, lo_node, level)
        elif not has_level:
            continue
        else:
            raise Exception(f"Wrong character in column {header}: '{has_level}'")


def add_learning_objective(g: Graph, row: Dict):
    lo_node = URIRef(PREFIX_LO + row[HEADER_LO_ID])

    _add_definitions(g, lo_node, row)
    _add_competency_levels(g, lo_node, row)
    _add_qualification_levels(g, lo_node, row)
