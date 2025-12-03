from sys import argv, stdout
import json
import semver
import yaml
import os

args = argv[1:]
assert len(args) >= 1, "ERROR: The script requires the file path as the first argument!"
conandata_path = args[0]
versions_range = 1

# Pick the number of versions to return
if len(args) >= 2:
    try:
        versions_range = int(args[1])
    except:
        print(f"WARNING: Version count argument value is not a valid numer, defaulting to: {versions_range}")

assert os.path.isfile(conandata_path), f"ERROR: This given path '{conandata_path}' is not a valid file!"
conandata_file = open(conandata_path, 'r')

# Try to load the yaml file
conandata_yaml = yaml.safe_load(conandata_file)
assert conandata_yaml != None, f"ERROR: Failed to parse '{conandata_path}' file as YAML content!"
assert conandata_yaml['sources'] != None, f"ERROR: Failed to access 'sources' key in '{conandata_path}' YAML file!"

# Get all version values and parser them with semver
versions = []
for key, value in conandata_yaml['sources'].items():
    versions.append(semver.Version.parse(key))

# Sort descending, from newest to oldest
versions.sort(reverse=True)

# Output json into the standard output
stdout.write(json.dumps([str(item) for item in versions[:versions_range]]))
