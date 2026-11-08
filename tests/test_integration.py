import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from database.database import get_connection


def test_has_transactions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM transactions
    """)

    count = cursor.fetchone()[0]

    conn.close()

    assert count > 0


def test_bnp_exists():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM bank_sent
    WHERE bank_origin='BNP'
    """)

    count = cursor.fetchone()[0]

    conn.close()

    assert count == 1


def test_sg_exists():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM bank_sent
    WHERE bank_origin='SG'
    """)

    count = cursor.fetchone()[0]

    conn.close()

    assert count == 1


def test_large_transaction_exists():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM transactions
    WHERE flag_gt_5000 = 1
    """)

    count = cursor.fetchone()[0]

    conn.close()

    assert count > 0