from csv2graph.cluster import add_cluster
from test.util import graph, same_graphs


def test_add_same_cluster_twice():
    g = graph()
    add_cluster(g, "42", {"de": "Label in Deutsch", "en": "Label in English"})
    add_cluster(g, "42", {"de": "Label in Deutsch", "en": "Label in English"})

    expected = graph().parse(data="""
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix tc: <http://lzfdm.nfdi.de/vocab/themencluster#> .

        tc:42 rdfs:label "Label in Deutsch"@de, "Label in English"@en .
    """)

    assert same_graphs(g, expected)
