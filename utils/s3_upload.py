import boto3

def upload_to_s3(filepath, filename):
    s3 = boto3.client("s3", region_name="ap-south-1")

    bucket_name = "ai-resume-tracker-analysis"

    s3.upload_file(filepath, bucket_name, filename)