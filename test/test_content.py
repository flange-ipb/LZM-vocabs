import pytest

from csv2graph.content import add_content
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
