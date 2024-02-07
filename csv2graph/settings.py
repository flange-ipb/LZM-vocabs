from csv2graph.namespace import kompetenz, lernniveaustufe, zielgruppe

#
# Headers in CSV file "LO-Matrix_Tischvorlage_cluster_1.xlsx - Matrix_de_en_gesamt.csv"
#
HEADER_LO_ID = "ID"
HEADER_CLUSTER_ID = "ID2"
HEADER_CLUSTER_DE = "Themencluster"
HEADER_CLUSTER_EN = "Cluster"
HEADER_TOPIC_ID_IN_CLUSTER = "Th.id"
HEADER_TOPIC_DE = "Themen"
HEADER_TOPIC_EN = "Content aspect"
HEADER_LO_DE = "Lernziele\n\nLernende können…"
HEADER_LO_EN = "Learning objectives\n\nLearners are able to…"
HEADER_SK_LEVEL = "SK\nPC\nlev."
HEADER_MK_LEVEL = "MK\nMC\nlev."
HEADER_SEK_LEVEL = "SeK SelfC\nlev."
HEADER_SOK_LEVEL = "SoK\nSC\nlev."
HEADER_BA = "BA"
HEADER_MA = "MA"
HEADER_PHD = "PHD\n"
HEADER_DATA = "Data"

#
# Language -> Header associations
#
LANG_DE = "de"
LANG_EN = "en"

CLUSTER_HEADER_LANGUAGE_ASSOCIATION = {
    LANG_DE: HEADER_CLUSTER_DE,
    LANG_EN: HEADER_CLUSTER_EN,
}

TOPIC_HEADER_LANGUAGE_ASSOCIATION = {
    LANG_DE: HEADER_TOPIC_DE,
    LANG_EN: HEADER_TOPIC_EN,
}

LO_HEADER_LANGUAGE_ASSOCIATION = {
    LANG_DE: HEADER_LO_DE,
    LANG_EN: HEADER_LO_EN,
}

#
# Header -> Competency association
#
HEADER_COMPETENCY_ASSOCIATION = {
    HEADER_SK_LEVEL: kompetenz.SK,
    HEADER_MK_LEVEL: kompetenz.MK,
    HEADER_SEK_LEVEL: kompetenz.SeK,
    HEADER_SOK_LEVEL: kompetenz.SoK,
}

#
# Field value -> Learning level associations inside the competency column
#
LEARNING_LEVELS_ASSOCIATION = {
    "1": lernniveaustufe.LNS1,
    "2": lernniveaustufe.LNS2,
    "3": lernniveaustufe.LNS3,
    "4": lernniveaustufe.LNS4,
    "5": lernniveaustufe.LNS5,
    "6": lernniveaustufe.LNS6,
}

#
# Header -> Qualification level association
#
HEADER_QUALIFICATION_LEVELS_ASSOCIATION = {
    HEADER_BA: zielgruppe.BA,
    HEADER_MA: zielgruppe.MA,
    HEADER_PHD: zielgruppe.PHD,
    HEADER_DATA: zielgruppe.DATA,
}

#
# Prefixes
#
PREFIX_LO = "http://lzfdm.nfdi.de/vocab/lernziel#"
PREFIX_CLUSTER = "http://lzfdm.nfdi.de/vocab/themencluster#"
PREFIX_TOPIC = "http://lzfdm.nfdi.de/vocab/thema#"
