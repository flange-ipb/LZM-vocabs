from csv2graph.learning_objective import add_learning_objective
from csv2graph.settings import HEADER_LO_ID, HEADER_LO_DE, HEADER_LO_EN
from test.util import graph, same_graphs


def test_add_learning_objective():
    g = graph()
    row = {
        HEADER_LO_ID: "12345",
        HEADER_LO_DE: "Definition in Deutsch",
        HEADER_LO_EN: "Definition in English",
    }
    add_learning_objective(g, row)

    expected = graph().parse(data="""
        @prefix lz: <http://lzfdm.nfdi.de/vocab/lernziel#> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

        lz:12345 skos:definition "Definition in Deutsch"@de, "Definition in English"@en .
    """)

    assert same_graphs(g, expected)
