# LZM-vocabs
Transformation der Lernzielmatrix zum Themenbereich Forschungsdatenmanagement (FDM) zu RDF (Resource Description Framework).

Dieses Git-Repo ist experimentell.

## Anleitung

### Installation
Voraussetzungen:
* Python 3
* pip (Paketverwaltungsprogramm für Python)

Dieses Git-Repository klonen:
```
git clone https://github.com/flange-ipb/LZM-vocabs.git
```

Eine virtualenv einrichten und aktivieren:
```
cd LZM-vocabs
python3 -m venv .env
source .env/bin/activate
```

Abhängigkeiten installieren:
```
pip install -r requirements.txt
```

Tests ausführen (optional):
```
pytest
```

### Tabellen
* Datei __LO-Matrix_Tischvorlage_gesamt.xlsx - Matrix_de_en_gesamt.csv__: exportiere das Tabellenblatt *Matrix_de_en_gesamt* aus der Tischvorlage als CSV
* Datei __LO-Matrix_Tischvorlage_gesamt.xlsx - Index.csv__: exportiere das Tabellenblatt *Index* aus der Tischvorlage als CSV

### Die Transformation ausführen
```
python -m csv2graph.csv2graph_main "LO-Matrix_Tischvorlage_gesamt.xlsx - Matrix_de_en_gesamt.csv" "LO-Matrix_Tischvorlage_gesamt.xlsx - Index.csv" output.ttl
```
Der RDF-Graph wird in die Datei _output.ttl_ im Turtle-Format geschrieben.
