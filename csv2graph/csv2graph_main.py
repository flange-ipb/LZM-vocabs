import argparse
import csv
import sys

from rdflib import Graph

from csv2graph.learning_objective import add_learning_objective
from csv2graph.util import graph


def _parse_args():
    parser = argparse.ArgumentParser(description="Lernzielmatrix CSV files to RDF graph.")
    parser.add_argument("csv_matrix", metavar="Matrix_de_en_gesamt",
                        help="the CSV file with the 'Matrix_de_en_gesamt' table")
    return parser.parse_args()


def _csv_matrix_to_graph(csv_matrix: str, g: Graph):
    with open(csv_matrix, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row_number, row in enumerate(reader):
            trimmed_row = {k: v.strip() for k, v in row.items()}
            try:
                add_learning_objective(g, trimmed_row)
            except Exception as e:
                print(f"Exception in row #{row_number + 2}: {str(e)}", file=sys.stderr)


def main() -> int:
    args = _parse_args()
    g = graph()

    _csv_matrix_to_graph(args.csv_matrix, g)
    print(g.serialize())

    return 0


if __name__ == '__main__':
    sys.exit(main())
