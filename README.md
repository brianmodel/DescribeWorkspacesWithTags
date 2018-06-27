# DescribeWorkspacesWithTags
Describe AWS workspaces with their respective tags.

The describe_workspaces_with_tags function returns an array of dictionarys that contain information of each workspace, including 
its respective tags.

The print_workspaces function is simply a nice way to print out a dictionary onto the command line in a readable way.

# Sample Output
{<br/>
    "ResponseMetadata": {<br/>
        "HTTPHeaders": {<br/>
            "content-length": "409",<br/>
            "content-type": "application/x-amz-json-1.1",<br/>
            "date": "Wed, 27 Jun 2018 01:04:33 GMT",<br/>
            "x-amzn-requestid": "12341234-1234-1234-b2e6-123456712345"<br/>
        },
        "HTTPStatusCode": 200,
        "RequestId": "12341234-1234-1234-1234-123412341234",
        "RetryAttempts": 0
    },
    "Tags": [
        {
            "Key": "Dept",
            "Value": "Finance"
        },
        {
            "Key": "Region",
            "Value": "US"
        },
        {
            "Key": "Name",
            "Value": "Test"
        }
    ],
    "Workspaces": [
        {
            "BundleId": "123-123412341",
            "ComputerName": "IP-12341234",
            "DirectoryId": "d-1234123412",
            "IpAddress": "12.3.4.123",
            "ModificationStates": [],
            "State": "AVAILABLE",
            "SubnetId": "subnet-12341234",
            "UserName": "test",
            "WorkspaceId": "ws-123412343",
            "WorkspaceProperties": {
                "ComputeTypeName": "PERFORMANCE",
                "RootVolumeSizeGib": 80,
                "RunningMode": "ALWAYS_ON",
                "UserVolumeSizeGib": 100
            }
        }
    ]
}
