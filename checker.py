#!/usr/bin/env python3

import yaml

with open('postgresql-chart/values.yaml') as f:
    md_dictionary = {}
    data = yaml.load(f, Loader=yaml.FullLoader)
    for k, v  in data.items():
        if isinstance(v,dict):
            for k2, v2 in v.items():
                if isinstance(v2,dict):
                    for k3, v3 in v2.items():
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
file_content = [ line for line in open('README.md') ]

for k_all in md_dictionary:
    md_key = "`" + k_all + "`"
    md_value = "`" + md_dictionary[k_all] + "`"
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
            else:
                raise ValueError("change the value of " + md_key + " in README.md")
        if len(file_content) == i and missing_in_readme:
            raise Exception(md_key + " does not exist in README")
print("README is synchronized with the parameters in postgresql-chart/values.yaml")
