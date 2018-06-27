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
        },<br/>
        "HTTPStatusCode": 200,<br/>
        "RequestId": "12341234-1234-1234-1234-123412341234",<br/>
        "RetryAttempts": 0<br/>
    },<br/>
    "Tags": [<br/>
        {<br/>
            "Key": "Dept",<br/>
            "Value": "Finance"<br/>
        },<br/>
        {<br/>
            "Key": "Region",<br/>
            "Value": "US"<br/>
        },<br/>
        {<br/>
            "Key": "Name",<br/>
            "Value": "Test"<br/>
        }<br/>
    ],<br/>
    "Workspaces": [<br/>
        {<br/>
            "BundleId": "123-123412341",<br/>
            "ComputerName": "IP-12341234",<br/>
            "DirectoryId": "d-1234123412",<br/>
            "IpAddress": "12.3.4.123",<br/>
            "ModificationStates": [],<br/>
            "State": "AVAILABLE",<br/>
            "SubnetId": "subnet-12341234",<br/>
            "UserName": "test",<br/>
            "WorkspaceId": "ws-123412343",<br/>
            "WorkspaceProperties": {<br/>
                "ComputeTypeName": "PERFORMANCE",<br/>
                "RootVolumeSizeGib": 80,<br/>
                "RunningMode": "ALWAYS_ON",<br/>
                "UserVolumeSizeGib": 100<br/>
            }<br/>
        }<br/>
    ]<br/>
}<br/>
