from typing import Dict, List

from rdflib import Graph, RDF, SKOS
from rdflib.plugins.sparql import prepareQuery
from rdflib.term import Node, BNode, Literal

from csv2graph.namespace import fdmontology
from csv2graph.settings import COL_TOPIC_DE, LANGUAGE_CONTENT_COL_ID_ASSOCIATION, LANG_DE


def add_content(g: Graph, definitions_dict: Dict) -> Node:
    content_node = BNode()
    g.add((content_node, RDF.type, fdmontology.Inhalt))
    for lang, definition in definitions_dict.items():
        g.add((content_node, SKOS.definition, Literal(definition, lang=lang)))

    return content_node


def _find_topic_by_label(g: Graph, label: str, lang: str) -> Node:
    q = prepareQuery("""
        PREFIX o: <http://lzfdm.nfdi.de/ontologie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?topic
        WHERE {
            ?topic a o:Thema .
            ?topic rdfs:label ?label
            FILTER(LCASE(?label) = LCASE(?input_label)) .
        }
    """)
    result = g.query(q, initBindings={"input_label": Literal(label, lang=lang)})

    if len(result) == 0:
        raise Exception(f"No topic with the label '{label}' found")
    if len(result) > 1:
        raise Exception(f"Found multiple topics with the same label '{label}'")

    return next(iter(result)).topic


def add_content_to_topic(g: Graph, row: List):
    content_definitions = {lang: row[col_id] for lang, col_id in LANGUAGE_CONTENT_COL_ID_ASSOCIATION.items()}
    content_node = add_content(g, content_definitions)

    topic_node = _find_topic_by_label(g, row[COL_TOPIC_DE], LANG_DE)
    g.add((topic_node, fdmontology.beinhaltetInhalt, content_node))
