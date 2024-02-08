from typing import Dict

from rdflib import Graph, URIRef, SKOS, RDF
from rdflib.term import Node, Literal, BNode

from csv2graph import topic, cluster
from csv2graph.namespace import fdmontology
from csv2graph.settings import (
    PREFIX_LO,
    HEADER_LO_ID,
    LANGUAGE_TO_LO_HEADER_ASSOCIATION,
    HEADER_TO_COMPETENCY_ASSOCIATION,
    LEARNING_LEVELS_ASSOCIATION,
    HEADER_TO_QUALIFICATION_LEVELS_ASSOCIATION,
    HEADER_TOPIC_ID_IN_CLUSTER,
    HEADER_CLUSTER_ID,
    LANGUAGE_TO_TOPIC_HEADER_ASSOCIATION,
    LANGUAGE_TO_CLUSTER_HEADER_ASSOCIATION,
)

_BEGINNING_OF_DEFINITION_TO_BE_REMOVED = (
    "...",
    "..",
    ".",
    "…",
)


def _clean_definition(definition: str) -> str:
    for to_remove in _BEGINNING_OF_DEFINITION_TO_BE_REMOVED:
        if definition.startswith(to_remove):
            definition = definition.removeprefix(to_remove)
    return definition.strip()


_PREFIX_OF_DEFINITION = {
    "de": "Lernende können ",
    "en": "Learners are able to ",
}


def _add_prefix_to_definition(definition: str, lang: str) -> str:
    return _PREFIX_OF_DEFINITION[lang] + definition


def _add_definitions(g: Graph, lo_node: Node, row: Dict):
    for lang, header in LANGUAGE_TO_LO_HEADER_ASSOCIATION.items():
        definition = _clean_definition(row[header])
        definition = _add_prefix_to_definition(definition, lang)

        g.add((lo_node, SKOS.definition, Literal(definition, lang=lang)))


def _add_competency_level(g: Graph, lo_node: Node, competency: Node, learning_level: Node):
    cl_node = BNode()
    g.add((lo_node, fdmontology.fördertKompetenzstufe, cl_node))
    g.add((cl_node, RDF.type, fdmontology.Kompetenzstufe))

    g.add((cl_node, fdmontology.weistKompetenzZu, competency))
    #g.add((competency, fdmontology.wirdZuKompetenzstufeZugewiesen, cl_node))

    g.add((cl_node, fdmontology.weistLernniveaustufeZu, learning_level))
    #g.add((learning_level, fdmontology.wirdZuKompetenzstufeZugewiesen2, cl_node))


def _add_competency_levels(g: Graph, lo_node: Node, row: Dict):
    for header, competency in HEADER_TO_COMPETENCY_ASSOCIATION.items():
        if learning_level := row[header]:
            _add_competency_level(g, lo_node, competency, LEARNING_LEVELS_ASSOCIATION[learning_level])


def _add_qualification_level(g: Graph, lo_node: Node, level_node: Node):
    g.add((lo_node, fdmontology.istAbgestimmtAufZielgruppe, level_node))
    g.add((level_node, fdmontology.istZielgruppeVonLernziel, lo_node))


def _add_qualification_levels(g: Graph, lo_node: Node, row: Dict):
    for header, level in HEADER_TO_QUALIFICATION_LEVELS_ASSOCIATION.items():
        has_level = row[header]
        if has_level.upper() == "X":
            _add_qualification_level(g, lo_node, level)
        elif not has_level:
            continue
        else:
            raise Exception(f"Wrong character in column {header}: '{has_level}'")


def _add_topic(g: Graph, lo_node: Node, row: Dict) -> Node:
    topic_labels = {lang: row[header] for lang, header in LANGUAGE_TO_TOPIC_HEADER_ASSOCIATION.items()}
    topic_node = topic.add_topic(g, row[HEADER_CLUSTER_ID], row[HEADER_TOPIC_ID_IN_CLUSTER], topic_labels)

    g.add((lo_node, fdmontology.adressiertThema, topic_node))
    g.add((topic_node, fdmontology.umfasstLernziel, lo_node))

    return topic_node


def _add_cluster_to_topic(g: Graph, topic_node: Node, row: Dict):
    cluster_labels = {lang: row[header] for lang, header in LANGUAGE_TO_CLUSTER_HEADER_ASSOCIATION.items()}
    cluster_node = cluster.add_cluster(g, row[HEADER_CLUSTER_ID], cluster_labels)

    g.add((cluster_node, fdmontology.enthältThema, topic_node))
    g.add((topic_node, fdmontology.gehörtZuThemenbereich, cluster_node))


def add_learning_objective(g: Graph, row: Dict):
    lo_node = URIRef(PREFIX_LO + row[HEADER_LO_ID])
    g.add((lo_node, RDF.type, fdmontology.Lernziel))

    _add_definitions(g, lo_node, row)
    _add_competency_levels(g, lo_node, row)
    _add_qualification_levels(g, lo_node, row)

    topic_node = _add_topic(g, lo_node, row)
    _add_cluster_to_topic(g, topic_node, row)
