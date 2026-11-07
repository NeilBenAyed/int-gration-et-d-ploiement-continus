from pathlib import Path
import pandas as pd

Path("storage/incoming").mkdir(
    parents=True,
    exist_ok=True
)

columns = [
    "transaction_datetime",
    "amount",
    "iban_origin",
    "country_origin",
    "bank_origin",
    "iban_dest",
    "country_dest"
]

transactions_01 = [
    [
        "2026-01-01 10:00:00",
        1000,
        "FR761111111111",
        "FR",
        "BNP",
        "FR762222222222",
        "FR"
    ],
    [
        "2026-01-01 11:00:00",
        2000,
        "FR761111111111",
        "FR",
        "BNP",
        "FR763333333333",
        "BE"
    ],
    [
        "2026-01-01 12:00:00",
        6000,
        "FR764444444444",
        "FR",
        "SG",
        "FR762222222222",
        "FR"
    ]
]

transactions_02 = [
    [
        "2026-01-02 10:00:00",
        3000,
        "FR761111111111",
        "FR",
        "BNP",
        "FR762222222222",
        "FR"
    ],
    [
        "2026-01-02 11:00:00",
        1500,
        "FR764444444444",
        "FR",
        "SG",
        "FR765555555555",
        "ES"
    ]
]

df1 = pd.DataFrame(
    transactions_01,
    columns=columns
)

df2 = pd.DataFrame(
    transactions_02,
    columns=columns
)

df1.to_csv(
    "storage/incoming/transactions_01.csv",
    index=False
)

df2.to_csv(
    "storage/incoming/transactions_02.csv",
    index=False
)

print("CSV générés avec succès")