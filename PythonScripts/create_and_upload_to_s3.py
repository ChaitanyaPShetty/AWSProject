import boto3

s3 = boto3.client('s3')
bucket_name = 'chaitanya-demo-bucket-001'

# Create bucket
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' created.")

# Upload file
s3.upload_file('sample.txt', bucket_name, 'sample.txt')
print("File uploaded to S3.")
