import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from storage.s3_client import get_s3_client


client = get_s3_client()

print("Connexion S3 réussie")