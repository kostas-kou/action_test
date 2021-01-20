#!/usr/bin/env python3

import yaml

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

#with open('postgresql-chart/values.yaml') as f:
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
#file_content = [ line for line in open('postgresql-chart/README_test.md') ]

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
            #print(line)
            line_split = line.split(" | ")
            #print(str(line_split[-1]))
            #print(str(md_value))
            if str(md_value) in str(line_split[-1]):
                continue
            elif md_value == None and "nil" in line_split[-1]:
                continue
            else:
                parameters_modify.append(md_key)
                #raise ValueError("change the value of " + md_key + " in README.md")
        if len(file_content) == i and missing_in_readme:
            parameters_missing.append(md_key)
            #raise Exception(md_key + " does not exist in README")

if len(parameters_missing) == 0 and len(parameters_modify) == 0: 
    print("README is synchronized with the parameters in postgresql-chart/values.yaml")
else:
    changes = True
    if len(parameters_modify) != 0:
        print(colours.fg.red, "Values need to be changed in README:", colours.reset)
        for modify in parameters_modify:
            print(colours.fg.yellow, modify, colours.reset)
    if len(parameters_missing) != 0:
        print("Parameters missing from README file:")
        for missing in parameters_missing:
            print(colours.fg.yellow, missing, colours.reset)
    #raise ValueError("Make all the above changes in README.md")

if changes:
    raise ValueError("Sync the values of the parameters in README with postgresql-chart/values.yaml")
