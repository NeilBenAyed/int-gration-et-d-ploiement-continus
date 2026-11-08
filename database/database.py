import sqlite3


def create_connection():
    """
    Crée la connexion à la base SQLite.
    """

    conn = sqlite3.connect(
        "database/transactions.db"
    )

    return conn


def create_tables():
    """
    Crée les tables de la base.
    """

    conn = create_connection()

    cursor = conn.cursor()

    # Table des transactions

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_datetime TEXT,
        amount REAL,
        iban_origin TEXT,
        country_origin TEXT,
        bank_origin TEXT,
        iban_dest TEXT,
        country_dest TEXT,
        flag_gt_5000 INTEGER
    )
    """)

    # Somme envoyée par IBAN

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iban_sent (
        iban_origin TEXT PRIMARY KEY,
        total_sent REAL
    )
    """)

    # Somme envoyée par banque

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bank_sent (
        bank_origin TEXT PRIMARY KEY,
        total_sent REAL
    )
    """)

    # Somme reçue par IBAN

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iban_received (
        iban_dest TEXT PRIMARY KEY,
        total_received REAL
    )
    """)

    # Fichiers déjà traités

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS processed_files (
        filename TEXT PRIMARY KEY
    )
    """)

    conn.commit()

    conn.close()

    print("Tables créées avec succès")


def insert_transactions(df):

    conn = create_connection()

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT INTO transactions (
            transaction_datetime,
            amount,
            iban_origin,
            country_origin,
            bank_origin,
            iban_dest,
            country_dest,
            flag_gt_5000
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["transaction_datetime"],
            row["amount"],
            row["iban_origin"],
            row["country_origin"],
            row["bank_origin"],
            row["iban_dest"],
            row["country_dest"],
            int(row["flag_gt_5000"])
        ))

    conn.commit()

    conn.close()

    print("Transactions insérées")