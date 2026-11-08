import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from storage.s3_client import download_file

download_file(
    "transactions",
    "transactions_01.csv",
    "storage/downloaded_transactions_01.csv"
)

download_file(
    "transactions",
    "transactions_02.csv",
    "storage/downloaded_transactions_02.csv"
)