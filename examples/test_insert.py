import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from processing.loader import load_csv
from processing.transformations import flag_large_transactions

from database.database import (
    create_tables,
    insert_transactions
)

create_tables()

df = load_csv(
    "storage/incoming/transactions_01.csv"
)

df = flag_large_transactions(df)

insert_transactions(df)