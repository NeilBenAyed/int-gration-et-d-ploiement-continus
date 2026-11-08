import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from database.database import get_connection


def test_transactions_exist():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM transactions
    """)

    count = cursor.fetchone()[0]

    conn.close()

    assert count > 0
