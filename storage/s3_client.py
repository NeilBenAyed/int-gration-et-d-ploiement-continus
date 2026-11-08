import boto3
from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed


def get_s3_client():

    return boto3.client(
        "s3",
        endpoint_url="http://localhost:8333",
        aws_access_key_id="admin",
        aws_secret_access_key="admin",
        region_name="us-east-1"
    )


def create_bucket(bucket_name):

    client = get_s3_client()

    try:

        client.create_bucket(
            Bucket=bucket_name
        )

        print(
            f"Bucket créé : {bucket_name}"
        )

    except Exception:

        print(
            f"Bucket déjà présent : {bucket_name}"
        )
def upload_file(
        local_file,
        bucket_name,
        object_name
):

    client = get_s3_client()

    client.upload_file(
        local_file,
        bucket_name,
        object_name
    )

    print(
        f"Upload réussi : {object_name}"
    )
@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2)
)
def download_file(
    bucket_name,
    object_name,
    local_file
):

    client = get_s3_client()

    client.download_file(
        bucket_name,
        object_name,
        local_file
    )

    print(
        f"Téléchargement réussi : {object_name}"
    )