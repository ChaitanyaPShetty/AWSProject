import boto3

# Instance details
INSTANCE_ID = "i-0a93410a7d393bd7d"
REGION = "us-east-1"

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name=REGION)

# Describe the specific instance
response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])

# Extract instance data
instance = response['Reservations'][0]['Instances'][0]

# Print metadata
print("✅ EC2 Instance Metadata")
print("------------------------")
print(f"Instance ID: {instance['InstanceId']}")
print(f"Instance Type: {instance['InstanceType']}")
print(f"AMI ID: {instance['ImageId']}")
print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
print(f"Private IP: {instance.get('PrivateIpAddress', 'N/A')}")
print(f"State: {instance['State']['Name']}")
print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
print(f"VPC ID: {instance.get('VpcId', 'N/A')}")
print(f"Subnet ID: {instance.get('SubnetId', 'N/A')}")
print(f"Launch Time: {instance['LaunchTime']}")
