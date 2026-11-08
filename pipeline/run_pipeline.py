import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from data_generator.generate_csv import *
from processing.loader import load_csv
from processing.transformations import (
    flag_large_transactions
)

from database.database import (
    create_tables,
    insert_transactions
)


def run():

    print("Etape 1 : génération des CSV")

    # le simple import a déjà généré les CSV

    print("Etape 2 : création de la base")

    create_tables()

    print("Etape 3 : chargement du csv")

    df = load_csv(
        "storage/incoming/transactions_01.csv"
    )

    print("Etape 4 : transformations")

    df = flag_large_transactions(df)

    print("Etape 5 : insertion")

    insert_transactions(df)

    print("Pipeline terminée")


if __name__ == "__main__":
    run()