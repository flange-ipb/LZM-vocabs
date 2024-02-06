from csv2graph.topic import add_topic
from test.util import graph, same_graphs


def test_add_same_topic_twice():
    g = graph()
    add_topic(g, "1", "42", {"de": "Label in deutsch", "en": "Label in english"})
    add_topic(g, "1", "42", {"de": "Label in deutsch", "en": "Label in english"})

    expected = graph().parse(data="""
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix thema: <http://lzfdm.nfdi.de/vocab/thema#> .

        thema:1-42 rdfs:label "Label in deutsch"@de, "Label in english"@en .
    """)

    assert same_graphs(g, expected)