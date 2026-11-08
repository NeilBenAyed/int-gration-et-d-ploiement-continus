import sqlite3

conn = sqlite3.connect("database/transactions.db")

cursor = conn.cursor()

print("\nTRANSACTIONS")
cursor.execute("SELECT * FROM transactions")
for row in cursor.fetchall():
    print(row)

print("\nBANK_SENT")
cursor.execute("SELECT * FROM bank_sent")
for row in cursor.fetchall():
    print(row)

print("\nIBAN_SENT")
cursor.execute("SELECT * FROM iban_sent")
for row in cursor.fetchall():
    print(row)

print("\nIBAN_RECEIVED")
cursor.execute("SELECT * FROM iban_received")
for row in cursor.fetchall():
    print(row)

conn.close()