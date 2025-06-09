from sys import argv
import yaml
import os

args = argv[1:]
error = "The script requires 1 argument (got {}) in the following order: expected-clang-version".format(len(args))
assert len(args) == 1, error

# Get all the arguments
file_name = os.path.join(os.path.expanduser("~"), ".conan2/settings.yml")
clang_version = args[0]

# Load the INI file
settings = yaml.load(open(file_name, 'r'), Loader=yaml.FullLoader)
versions = settings['compiler']['clang']['version']


if clang_version not in versions:
    versions.append(clang_version)
    settings['compiler']['clang']['version'] = versions

    with open(file_name, 'w') as yaml_file:
        yaml_file.write( yaml.dump(settings) )
