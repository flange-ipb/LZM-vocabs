"""
Terms from the FDM-LZM ontology
"""
from rdflib import URIRef

NS = "http://lzfdm.nfdi.de/ontologie/"

#
# Classes
#
Lernziel = URIRef(NS + "Lernziel")
Kompetenzstufe = URIRef(NS + "Kompetenzstufe")
Inhalt = URIRef(NS + "Inhalt")
Kompetenz = URIRef(NS + "Kompetenz")
Zielgruppe = URIRef(NS + "Zielgruppe")
Thema = URIRef(NS + "Thema")
Themenbereich = URIRef(NS + "Themenbereich")
Lernniveaustufe = URIRef(NS + "Lernniveaustufe")

#
# Properties
#
# Kompetenzstufe - Kompetenz
weistKompetenzZu = URIRef(NS + "weistKompetenzZu")
wirdZuKompetenzstufeZugewiesen = URIRef(NS + "wirdZuKompetenzstufeZugewiesen")

# Zielgruppe - Lernziel
istZielgruppeVonLernziel = URIRef(NS + "istZielgruppeVonLernziel")
istAbgestimmtAufZielgruppe = URIRef(NS + "istAbgestimmtAufZielgruppe")

# Thema - Inhalt
beinhaltetInhalt = URIRef(NS + "beinhaltetInhalt")
wirdBeinhaltetVonThema = URIRef(NS + "wirdBeinhaltetVonThema")

# Thema - Lernziel
umfasstLernziel = URIRef(NS + "umfasstLernziel")
adressiertThema = URIRef(NS + "adressiertThema")

# Lernziel - Lernziel
istVorausgesetztesLernzielVon = URIRef(NS + "istVorausgesetztesLernzielVon")
setztLernzielVoraus = URIRef(NS + "setztLernzielVoraus")

# Lernziel - Kompetenzstufe
fördertKompetenzstufe = URIRef(NS + "fördertKompetenzstufe")
# inverse missing

# Kompetenz - Lernziel
wirdGefördertVonLernziel = URIRef(NS + "wirdGefördertVonLernziel")
# inverse missing

# Thema - Themenbereich
gehörtZuThemenbereich = URIRef(NS + "gehörtZuThemenbereich")
enthältThema = URIRef(NS + "enthältThema")

# Kompetenzstufe - Lernniveaustufe
weistLernniveaustufeZu = URIRef(NS + "weistLernniveaustufeZu")
wirdZuKompetenzstufeZugewiesen2 = URIRef(NS + "wirdZuKompetenzstufeZugewiesen2")
