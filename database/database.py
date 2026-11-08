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

    # Historique des fichiers déjà traités

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


def is_file_processed(filename):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT filename
    FROM processed_files
    WHERE filename = ?
    """, (filename,))

    result = cursor.fetchone()

    conn.close()

    return result is not None


def mark_file_processed(filename):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO processed_files(filename)
    VALUES(?)
    """, (filename,))

    conn.commit()

    conn.close()

    print(f"Fichier marqué comme traité : {filename}")
    
def get_connection():

    return create_connection()
def insert_iban_sent(df):

    conn = create_connection()

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT OR REPLACE INTO iban_sent(
            iban_origin,
            total_sent
        )
        VALUES (?, ?)
        """, (
            row["iban_origin"],
            row["amount"]
        ))

    conn.commit()
    conn.close()

    print("Agrégat iban_sent inséré")
def insert_bank_sent(df):

    conn = create_connection()

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT OR REPLACE INTO bank_sent(
            bank_origin,
            total_sent
        )
        VALUES (?, ?)
        """, (
            row["bank_origin"],
            row["amount"]
        ))

    conn.commit()
    conn.close()

    print("Agrégat bank_sent inséré")
def insert_iban_received(df):

    conn = create_connection()

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute("""
        INSERT OR REPLACE INTO iban_received(
            iban_dest,
            total_received
        )
        VALUES (?, ?)
        """, (
            row["iban_dest"],
            row["amount"]
        ))

    conn.commit()
    conn.close()

    print("Agrégat iban_received inséré")