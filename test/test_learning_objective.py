from csv2graph.learning_objective import add_learning_objective
from csv2graph import settings
from test.util import graph, same_graphs


def test_add_learning_objective():
    g = graph()
    row = {
        settings.HEADER_LO_ID: "12345",
        settings.HEADER_LO_DE: "Definition in Deutsch",
        settings.HEADER_LO_EN: "Definition in English",
        settings.HEADER_SK_LEVEL: "",
        settings.HEADER_MK_LEVEL: "4",
        settings.HEADER_SEK_LEVEL: "2",
        settings.HEADER_SOK_LEVEL: "1",
        settings.HEADER_BA: "",
        settings.HEADER_MA: "",
        settings.HEADER_PHD: "X",
        settings.HEADER_DATA: "X",
    }
    add_learning_objective(g, row)

    expected = graph().parse(data="""
        @prefix komp: <http://lzfdm.nfdi.de/vocab/kompetenz#> .
        @prefix lns: <http://lzfdm.nfdi.de/vocab/lernniveaustufe#> .
        @prefix lz: <http://lzfdm.nfdi.de/vocab/lernziel#> .
        @prefix o: <http://lzfdm.nfdi.de/ontologie/> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        @prefix zg: <http://lzfdm.nfdi.de/vocab/qualifikationsstufe#> .

        lz:12345 o:fördertKompetenzstufe [
                a o:Kompetenzstufe ;
                o:weistKompetenzZu komp:SoK ;
                o:weistLernniveaustufeZu lns:1
            ],
            [
                a o:Kompetenzstufe ;
                o:weistKompetenzZu komp:SeK ;
                o:weistLernniveaustufeZu lns:2
            ],
            [
                a o:Kompetenzstufe ;
                o:weistKompetenzZu komp:MK ;
                o:weistLernniveaustufeZu lns:4
            ] ;
            o:istAbgestimmtAufZielgruppe zg:Data, zg:PhD ;
            skos:definition "Definition in Deutsch"@de, "Definition in English"@en .

        zg:Data o:istZielgruppeVonLernziel lz:12345 .
        zg:PhD o:istZielgruppeVonLernziel lz:12345 .
    """)

    assert same_graphs(g, expected)
