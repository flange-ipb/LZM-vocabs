import pytest

from csv2graph.topic import add_topic
from csv2graph.util import graph
from test.util import same_graphs


def test_add_same_topic_twice():
    g = graph()
    add_topic(g, "1", "42", {"de": "Label in Deutsch", "en": "Label in English"})
    add_topic(g, "1", "42", {"de": "Label in Deutsch", "en": "Label in English"})

    expected = graph().parse(data="""
        @prefix o: <http://lzfdm.nfdi.de/ontologie/> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix thema: <http://lzfdm.nfdi.de/vocab/thema#> .

        thema:1-42 a o:Thema ;
            rdfs:label "Label in Deutsch"@de, "Label in English"@en .
    """)

    assert same_graphs(g, expected)


def test_add_topic_raises_exception_when_missing_cluster_id():
    with pytest.raises(Exception):
        add_topic(graph(), "", "42", {"de": "Label in Deutsch", "en": "Label in English"})


def test_add_topic_raises_exception_when_missing_topic_id():
    with pytest.raises(Exception):
        add_topic(graph(), "1", "", {"de": "Label in Deutsch", "en": "Label in English"})
