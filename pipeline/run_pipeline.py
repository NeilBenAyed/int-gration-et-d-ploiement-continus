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
    insert_transactions,
    is_file_processed,
    mark_file_processed
)


def run():

    print("Etape 1 : génération des CSV")

    create_tables()

    files = os.listdir("storage/incoming")

    for file_name in files:

        if not file_name.endswith(".csv"):
            continue

        print(f"\nTraitement de {file_name}")

        if is_file_processed(file_name):

            print(
                f"{file_name} déjà traité - ignoré"
            )

            continue

        file_path = os.path.join(
            "storage/incoming",
            file_name
        )

        df = load_csv(file_path)

        df = flag_large_transactions(df)

        insert_transactions(df)

        mark_file_processed(file_name)

    print("\nPipeline terminée")


if __name__ == "__main__":
    run()
