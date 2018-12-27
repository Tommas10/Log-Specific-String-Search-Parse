#!/usr/bin/env python

# This Python (script) is keyword search, only copy part of string into another textfile. 
# This Python (Script) created by Tommas Huang

with open('/Users/TommasHuang/Documents/log1.txt', 'w') as wFile:
# Save search keyword result, and then copy part of string into another file path.
    with open('/Users/TommasHuang/Documents/log.txt', 'r') as verFile: 
    # Open original want to search file. Original file path.
        for line in verFile:
            if 'WiFi' in line:
                # Can change search keyword " if '___' in line
                # Split the line from the right on underscores and
                # take the last part of the resulting list.
                wFile.write(line.rpartition('_')[-1])