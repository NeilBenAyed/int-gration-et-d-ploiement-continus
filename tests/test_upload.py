import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from storage.s3_client import (
    create_bucket,
    upload_file
)

create_bucket("transactions")

upload_file(
    "storage/incoming/transactions_01.csv",
    "transactions",
    "transactions_01.csv"
)

upload_file(
    "storage/incoming/transactions_02.csv",
    "transactions",
    "transactions_02.csv"
)