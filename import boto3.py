import boto3

def get_s3_credentials():
    # Create a new session using your AWS credentials
    session = boto3.Session()

    # Get the default S3 client
    s3 = session.client('s3')

    # Retrieve the bucket name
    s3_bucket = 'helloayushi'

    # Retrieve the access key and secret key
    credentials = session.get_credentials()
    s3_access_key = credentials.access_key
    s3_secret_key = credentials.secret_key

    return s3_bucket, s3_access_key, s3_secret_key

# Usage
s3_bucket, s3_access_key, s3_secret_key = get_s3_credentials()
print("S3 Bucket:", s3_bucket)
print("Access Key:", s3_access_key)
print("Secret Key:", s3_secret_key)
