import pandas as pd


def load_csv(file_path):
    """
    Charge un fichier CSV et retourne un DataFrame Pandas.
    """
    return pd.read_csv(file_path)