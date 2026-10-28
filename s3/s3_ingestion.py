import boto3
import os
from dotenv import load_dotenv


load_dotenv()


AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
FILE_KEY = os.getenv("S3_FILE_KEY")


LOCAL_PATH = "data/raw/sales.csv"


s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)


def download_file():

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    s3.download_file(
        BUCKET_NAME,
        FILE_KEY,
        LOCAL_PATH
    )

    print("S3 file downloaded successfully")
    print(LOCAL_PATH)



if __name__ == "__main__":
    download_file()