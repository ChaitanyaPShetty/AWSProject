import boto3
import json

client = boto3.client('lambda')

payload = {
    "Records": [{
        "s3": {
            "bucket": {"name": "chaitanya-uploadlogs"},
            "object": {"key": "sample-from-script.txt"}
        }
    }]
}

response = client.invoke(
    FunctionName='LogS3Lambda',
    InvocationType='RequestResponse',
    Payload=json.dumps(payload),
)

print(response['Payload'].read().decode())
