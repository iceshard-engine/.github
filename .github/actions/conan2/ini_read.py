from sys import argv, stdout
from configparser import ConfigParser

args = argv[1:]
error = "The script requires 3 arguments (got {}) in the following order: file, section, key".format(len(args))
assert len(args) == 3, error

# Get all the arguments
file = args[0]
section = args[1]
key = args[2]

# Load the INI file
config = ConfigParser()
config.read(file)

# Add a new section and key-value pair
if section not in config:
    config.add_section(section)

# Write to output without a newline
stdout.write(config[section][key])
