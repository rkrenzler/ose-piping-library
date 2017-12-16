#!/usr/bin/python3
# Author: Ruslan Krenzler
# Date: 16 December 2017
# Use this file to convert long string copied from PDF
# to a python array.
# adjust the value of input_str and of the schedule.

import re

input_str = """401-003 3/8 3/8 3/8 1-1/8 1-1/8 2-1/4 31/32 .04
401-005 1/2 1/2 1/2 1-1/4 1-1/4 2-1/2 1-3/32 .06
401-007 3/4 9/16 9/16 1-9/16 1-9/16 3-1/8 1-5/16 .10
401-010 1 11/16 11/16 1-3/4 1-3/4 3-1/2 1-5/8 .16
401-012 1-1/4 7/8 7/8 2-1/8 2-1/8 4-1/4 2 .25
401-015 1-1/2 1-1/16 1-1/16 2-3/8 2-3/8 4-3/4 2-1/4 .33
401-020 2 1-3/8 1-3/8 2-3/4 2-3/4 5-1/2 2-3/4 .51
401-025 2-1/2 1-21/32 1-21/32 3-13/32 3-13/32 6-13/16 3-11/32 1.03"""

schedule = 40

def process_value(value):
    """Convert a technical value "1-1/8" to a python value
    "1+1/8.0"""
    # Replace "-" by "+"
    value = "+".join(value.split("-"))
    # Add .0 to a number when it appears after / to prevent
    # integer devision in python 2. We want 1/2 to be calculated "0.5"
    # and not "0". That is why we write "1/2.0". We prefere
    # "1/2.0" instead of 0.5 to have a notation which is close
    # to original technical notation.
    return re.sub(r'(/\d+)', r'\1.0', value)
    
    
def process_line(line, schedule):
    # Split in words separted by " ".
    words = line.split()
    # 0-th word contains a string value. Put it between quotation marks.
    zeroth = words.pop(0)
    result = "'"+zeroth+"\'"
    # 1-th word will be converted to astring with a quantity
    # with inch unite. That is 1/2->'1/2"'.
    first = words.pop(0)
    result += ", '"+first+'"\''
    # 2-word contains the scheduler value
    result += ", %d"%schedule
    for word in words:
        result+=", "+process_value(word)
    return result

result = ""
for line in input_str.splitlines():
    if len(result) == 0:
        result+="["
    else:
        result+=",\n"
    result+="["+process_line(line, schedule)+"]"
result+="]"    
print(result)
