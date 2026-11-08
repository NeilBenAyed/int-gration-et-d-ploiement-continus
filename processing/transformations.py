def amount_sent_by_iban(df):
    return (
        df.groupby("iban_origin")["amount"]
        .sum()
        .reset_index()
    )


def amount_sent_by_bank(df):
    return (
        df.groupby("bank_origin")["amount"]
        .sum()
        .reset_index()
    )


def amount_received_by_iban(df):
    return (
        df.groupby("iban_dest")["amount"]
        .sum()
        .reset_index()
    )


def flag_large_transactions(df):
    result = df.copy()

    result["flag_gt_5000"] = (
        result["amount"] > 5000
    )

    return result