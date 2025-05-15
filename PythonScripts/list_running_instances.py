import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]
)

print("Running EC2 instances:")
for res in response['Reservations']:
    for instance in res['Instances']:
        print(f"Instance ID: {instance['InstanceId']} - Public IP: {instance.get('PublicIpAddress', 'N/A')}")
