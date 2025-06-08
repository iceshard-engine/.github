from sys import argv
from configparser import ConfigParser

args = argv[1:]
error = "The script requires 4 arguments (got {}) in the following order: file, section, key, value".format(len(args))
assert len(args) == 4, error

# Get all the arguments
file = args[0]
section = args[1]
key = args[2]
value = args[3]

# Load the INI file
config = ConfigParser()
config.read(file)

# Add a new section and key-value pair
if section not in config:
    config.add_section(section)
config[section][key] = value

# Save changes back to the file
with open(file, 'w') as configfile:
    config.write(configfile,space_around_delimiters=False)
