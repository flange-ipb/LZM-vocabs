from csv2graph import settings as s
from csv2graph.learning_objective import add_learning_objective
from csv2graph.util import graph
from test.util import same_graphs


def test_add_learning_objective():
    g = graph()
    row = {
        s.HEADER_LO_ID: "12345",
        s.HEADER_CLUSTER_ID: "2",
        s.HEADER_CLUSTER_DE: "Label des Themenclusters",
        s.HEADER_CLUSTER_EN: "Label of the cluster",
        s.HEADER_TOPIC_ID_IN_CLUSTER: "5",
        s.HEADER_TOPIC_DE: "Label des Themas",
        s.HEADER_TOPIC_EN: "Label of the content aspect",
        s.HEADER_LO_DE: "Definition in Deutsch",
        s.HEADER_LO_EN: "Definition in English",
        s.HEADER_SK_LEVEL: "",
        s.HEADER_MK_LEVEL: "4",
        s.HEADER_SEK_LEVEL: "2",
        s.HEADER_SOK_LEVEL: "1",
        s.HEADER_BA: "",
        s.HEADER_MA: "",
        s.HEADER_PHD: "X",
        s.HEADER_DATA: "X",
    }
    add_learning_objective(g, row)

    expected = graph().parse(data="""
        @prefix komp: <http://lzfdm.nfdi.de/vocab/kompetenz#> .
        @prefix lns: <http://lzfdm.nfdi.de/vocab/lernniveaustufe#> .
        @prefix lz: <http://lzfdm.nfdi.de/vocab/lernziel#> .
        @prefix o: <http://lzfdm.nfdi.de/ontologie/> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
        @prefix tc: <http://lzfdm.nfdi.de/vocab/themencluster#> .
        @prefix thema: <http://lzfdm.nfdi.de/vocab/thema#> .
        @prefix zg: <http://lzfdm.nfdi.de/vocab/qualifikationsstufe#> .

        lz:12345 a o:Lernziel ;
            o:fördertKompetenzstufe [
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
            o:adressiertThema thema:2-5 ;
            skos:definition "Definition in Deutsch"@de, "Definition in English"@en .

        zg:Data o:istZielgruppeVonLernziel lz:12345 .
        zg:PhD o:istZielgruppeVonLernziel lz:12345 .

        thema:2-5 a o:Thema ;
            rdfs:label "Label des Themas"@de, "Label of the content aspect"@en ;
            o:gehörtZuThemenbereich tc:2 ;
            o:umfasstLernziel lz:12345 .

        tc:2 a o:Themenbereich ;
            rdfs:label "Label des Themenclusters"@de, "Label of the cluster"@en ;
            o:enthältThema thema:2-5 .
    """)

    assert same_graphs(g, expected)
