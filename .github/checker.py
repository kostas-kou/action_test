#!/usr/bin/env python3

import yaml

with open('postgresql-chart/values.yaml') as f:
#with open('postgresql-chart/values_test.yaml') as f:
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
                raise ValueError("change the value of " + md_key + " in README.md")
        if len(file_content) == i and missing_in_readme:
            raise Exception(md_key + " does not exist in README")
print("README is synchronized with the parameters in postgresql-chart/values.yaml")
