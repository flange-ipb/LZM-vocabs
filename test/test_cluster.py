import pytest

from csv2graph.cluster import add_cluster
from csv2graph.util import graph
from test.util import same_graphs


def test_add_same_cluster_twice():
    g = graph()
    add_cluster(g, "42", {"de": "Label in Deutsch", "en": "Label in English"})
    add_cluster(g, "42", {"de": "Label in Deutsch", "en": "Label in English"})

    expected = graph().parse(data="""
        @prefix o: <http://lzfdm.nfdi.de/ontologie/> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix tc: <http://lzfdm.nfdi.de/vocab/themencluster#> .

        tc:42 a o:Themenbereich ;
            rdfs:label "Label in Deutsch"@de, "Label in English"@en .
    """)

    assert same_graphs(g, expected)


def test_add_cluster_raises_exception_when_missing_cluster_id():
    with pytest.raises(Exception):
        add_cluster(graph(), "", {"de": "Label in Deutsch", "en": "Label in English"})
