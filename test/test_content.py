import pytest

from csv2graph.content import add_content, add_content_to_topic
from csv2graph.topic import add_topic
from test.util import graph, same_graphs


def test_add_content():
    g = graph()
    add_content(g, {"de": "Definition in Deutsch", "en": "Definition in English"})

    expected = graph().parse(data="""
        @prefix o: <http://lzfdm.nfdi.de/ontologie/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

        [] a o:Inhalt ;
            skos:definition "Definition in Deutsch"@de, "Definition in English"@en .
    """)

    assert same_graphs(g, expected)


def test_add_content_to_topic():
    g = graph()
    add_topic(g, "1", "42", {"de": "Label des Themas", "en": "Label of the topic"})

    add_content_to_topic(g, ["Col0 is ignored", "Label des Themas", "Col2 is ignored", "Definition des Inhalts"])

    expected = graph().parse(data="""
        @prefix o: <http://lzfdm.nfdi.de/ontologie/> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        @prefix thema: <http://lzfdm.nfdi.de/vocab/thema#> .

        thema:1-42 a o:Thema ;
            rdfs:label "Label des Themas"@de, "Label of the topic"@en ;
            o:beinhaltetInhalt [
                a o:Inhalt ;
                skos:definition "Definition des Inhalts"@de
            ] .
    """)

    assert same_graphs(g, expected)


def test_add_content_to_topic_without_existing_topic():
    g = graph()

    with pytest.raises(Exception):
        add_content_to_topic(g, ["Col0 is ignored", "Label des Themas", "Col2 is ignored", "Definition des Inhalts"])


def test_add_content_to_topic_with_many_topics_having_the_same_label():
    g = graph()
    add_topic(g, "1", "42", {"de": "Label des Themas", "en": "Label of the topic"})
    add_topic(g, "2", "42", {"de": "Label des Themas", "en": "Label of the topic"})

    with pytest.raises(Exception):
        add_content_to_topic(g, ["Col0 is ignored", "Label des Themas", "Col2 is ignored", "Definition des Inhalts"])
