import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from processing.loader import load_csv

from processing.transformations import (
    amount_sent_by_iban,
    amount_sent_by_bank,
    amount_received_by_iban,
    flag_large_transactions
)

df = load_csv(
    "storage/incoming/transactions_01.csv"
)

print("\n=== SOMME PAR IBAN ===")
print(amount_sent_by_iban(df))

print("\n=== SOMME PAR BANQUE ===")
print(amount_sent_by_bank(df))

print("\n=== SOMME RECUE ===")
print(amount_received_by_iban(df))

print("\n=== FLAG TRANSACTIONS ===")
print(flag_large_transactions(df))