#!/usr/bin/env python3 

import yaml

# Script for checking if the parameters' values are the same 
# in postgresql-chart/values.yaml and postgresql-chart/README.md files

# Class for coloured output in terminal
class colours:
    reset='\033[0m'
    # Frontground
    class fg:
        red='\033[31m'
        green='\033[32m'
        cyan='\033[36m'
        yellow='\033[93m'
    # Background
    class bg:
        red='\033[41m'
        green='\033[42m'

# Create a dictionary from values.yaml where the parameters 
# are in the same form as in README.md
with open('postgresql-chart/values.yaml') as f:
    md_dictionary = {}
    data = yaml.load(f, Loader=yaml.FullLoader)
    for k, v  in data.items():
        if isinstance(v,dict):
            for k2, v2 in v.items():
                if isinstance(v2,dict):
                    for k3, v3 in v2.items():
                        if isinstance(v3,dict):
                            for k4, v4 in v3.items():
                                key = k + "." + k2 + "." + k3 + "." + k4
                                value = v4
                                md_dictionary.update({key:value})
                        else:
                            key = k + "." + k2 + "." + k3
                            value = v3
                            md_dictionary.update({key:value})
                else:
                    key = k + "." + k2
                    value = v2
                    md_dictionary.update({key:value})
        else:
            key = k
            value = v
            md_dictionary.update({key:value})

# Load the file into file_content
file_content = [ line for line in open('postgresql-chart/README.md') ]

# Create list for parameters that need to be changed or missing
parameters_modify = []
parameters_missing = []
changes = False

# Loop for checking if the changes made in values.yaml have been made also in README
for k_all in md_dictionary:
    md_key = "`" + k_all + "`"
    if md_dictionary[k_all] == None:
        md_value = None
    elif isinstance(md_dictionary[k_all], bool):
        if md_dictionary[k_all]:
            md_value = "true"
        else:
            md_value = "false"
    elif isinstance(md_dictionary[k_all], list):
        if len(md_dictionary[k_all]) == 0:
            md_value = "`[]`"
        else:
            md_value = "`" + str(md_dictionary[k_all][0]) + "`"
    elif md_dictionary[k_all] == '':
        md_value = "''"
    else:
        md_value = md_dictionary[k_all]
    i = 0
    missing_in_readme = True
    for line in file_content:
        i = i + 1
        if line.startswith(md_key):
            missing_in_readme = False
            line_split = line.split(" | ")
            if str(md_value) in str(line_split[-1]):
                continue
            elif md_value == None and "nil" in line_split[-1]:
                continue
            else:
                parameters_modify.append(md_key)
        if len(file_content) == i and missing_in_readme:
            parameters_missing.append(md_key)

# Raise error for parameters in case that are not synchronised in the two files 
if len(parameters_missing) == 0 and len(parameters_modify) == 0: 
    print("README is synchronized with the parameters in postgresql-chart/values.yaml")
else:
    if len(parameters_modify) != 0:
        print(colours.fg.red, "Values need to be changed in README:", colours.reset)
        for modify in parameters_modify:
            print(colours.fg.yellow, modify, colours.reset)
    if len(parameters_missing) != 0:
        print("Parameters missing from README file:")
        for missing in parameters_missing:
            print(colours.fg.yellow, missing, colours.reset)
    changes = True
    
if changes:
    raise ValueError("Sync the values of the parameters in README with postgresql-chart/values.yaml")
    print(ValueError.args)
