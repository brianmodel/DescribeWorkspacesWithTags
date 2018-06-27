import boto3, json

def describe_workspaces_with_tags():
	'''
	Function that returns workspace information with tags.
	'''
	client = boto3.client('workspaces')

	# Getting the data from all the workspaces
	workspaces = client.describe_workspaces()['Workspaces']
	all_data = []

	for workspace in workspaces:

		# Getting id of the workspace
		_id = workspace['WorkspaceId']

		# Describing the specific workspace and getting the list of tags
		workspace_info = client.describe_workspaces(WorkspaceIds = [_id])
		tags = client.describe_tags(ResourceId = _id)['TagList']

		# Adding the tags list to the workspace_info dictionary, and adding it to all the data
		workspace_info['Tags'] = tags
		all_data.append(workspace_info)

	# Returning all the data in an array of dictionarys.
	return all_data


def print_workspaces(describe_workspaces):
	'''
	Function that prints out the data in a readable way.
	describe_workspaces parameter must be a dictionary.
	'''
	for workspace in describe_workspaces:
		print(json.dumps(workspace, indent=4, sort_keys=True))
		print('')

if __name__=="__main__":
	print_workspaces(describe_workspaces_with_tags())
