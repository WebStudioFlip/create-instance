import boto3


def connectToAWS():
    aws_access_key_id = 'ASIA4XXXXXXXXXN4EHR'
    aws_secret_access_key = 'pqXi0FlxxxxxxxxxxxbnLfECuPpvV/D8MaBsrd'
    aws_session_token = 'FwoGZXIvYxxxxxxxxxxxATzMSVCnEBoaGnD3n7BF2xu/KaNdLeALe3PlM5y/guBxpn598wj3PWOfU3SW4xxxxxxxemjhpgK2n8+h6lk0MnNR5ZrXQA2sK2W+nsRoI2bmIxxxxxxxxxxxxxxo/5mE6atpxxxxxxxxxxxxBIW7+4U3blwTkC/GDHKoJyU/Z1DlpwA4OCE9x0FnJIVRDDu+XUey+cXjF5e1+XwsH+PSrxqxxxxxxxxxxxxxxxxx3XHja2HTijSLZcohaThpQYyLfeEH/kWIlLzmiq+iRZ8NsaZMVysjt2z51YFTPfgjGIpBMpp50w5K7CfHa1MCw=='
    region = 'us-west-2'
    ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key, region_name=region, aws_session_token=aws_session_token)
    instance = ec2.create_instances(
        MaxCount=1,
        MinCount=1,
        ImageId="ami-0507f77897697c4ba",
        InstanceType="t2.micro",
        KeyName="vockey",
        EbsOptimized=False,
        NetworkInterfaces=[
            {
                "SubnetId": "subnet-0d6760e1fd978c897",
                "AssociatePublicIpAddress": True,
                "DeviceIndex": 0,
                "Groups": [
                    "sg-0f02bd7efee33b4ee"
                ]
            }
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
        ],
        PrivateDnsNameOptions={
            "HostnameType": "ip-name",
            "EnableResourceNameDnsARecord": False,
            "EnableResourceNameDnsAAAARecord": False
        }
    )


connectToAWS()
