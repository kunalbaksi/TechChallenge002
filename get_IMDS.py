import requests
import json

# Function to get metadata of the VM instance
def get_instance_md():
    imds_url = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
    headers = {'Metadata': 'true'}
    try:
        response = requests.get(imds_url, headers=headers)
        response.raise_for_status()

        # Parse JSON response
        metadata = response.json()
        return metadata
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Function to export metadata to a json file
def export_to_jsonfile(metadata, filename, key=None):
    with open(filename, 'w') as json_file:
        json.dump(metadata, json_file, indent=4)
    
this_vm_metadata = get_instance_md()

# Print JSON data
if this_vm_metadata:
    filename = "this_vm_metadata.json"
    export_to_jsonfile(this_vm_metadata, filename)
    print(f"This Azure VM metadata saved to '{filename}'")