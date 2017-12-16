#!/usr/bin/python3
# Author: Ruslan Krenzler
# Date: 16 December 2017
# Use this file to convert long string copied from PDF
# to a python array.
# adjust the value of input_str and of the schedule.

# The data is from https://www.aetnaplastics.com.

import re

schedule1 = 40
txt1 = """401-003 3/8 3/8 3/8 1-1/8 1-1/8 2-1/4 31/32 .04
401-005 1/2 1/2 1/2 1-1/4 1-1/4 2-1/2 1-3/32 .06
401-007 3/4 9/16 9/16 1-9/16 1-9/16 3-1/8 1-5/16 .10
401-010 1 11/16 11/16 1-3/4 1-3/4 3-1/2 1-5/8 .16
401-012 1-1/4 7/8 7/8 2-1/8 2-1/8 4-1/4 2 .25
401-015 1-1/2 1-1/16 1-1/16 2-3/8 2-3/8 4-3/4 2-1/4 .33
401-020 2 1-3/8 1-3/8 2-3/4 2-3/4 5-1/2 2-3/4 .51
401-025 2-1/2 1-21/32 1-21/32 3-13/32 3-13/32 6-13/16 3-11/32 1.03"""


schedule2 = 40
# The following text needed some manual postprocessing
txt2 = """401-030 3 1-15/16 1-15/16 3-27/32 3-27/32 7-11/16 4 1.43
401-040 4 2-13/32 2-13/32 4-7/16 4-7/16 8-7/8 5-1/32 2.22
401-050 5 3 3 6 6 12 6-5/32 4.59
401-060 6 3-5/8 3-5/8 6-21/32 6-21/32 13-5/16 7-9/32 6.00
401-080 8 4-1/2 4-1/2 8-17/32 8-17/32 17-1/16 9-3/8 11.81
401-100 10 5-13/16 5-13/16 10-27/32 10-27/32 21-11/16 11-21/32 24.25
401-100F 10 9-7/8 9-3/8 15-1/8 14-5/8 30-1/4 11-1/2 36.21
401-120 12 6-27/32 6-27/32 12-27/32 12-27/32 25-11/16 13-3/4 37.94
401-120F 12 10-3/4 10-3/16 17 16-7/16 34 13-9/16 56.32
401-140 14 7-1/32 7-1/32 14-7/32 14-1/32 28-7/16 15-21/32 64.02
401-140F 14 11-3/8 11 18-3/8 18 36-3/4 14-7/8 75.11
401-160F 16 15 12-7/8 23 20-7/8 46 17 111.00
401-180F 18 15-7/8 13-3/8 24-7/8 22-3/8 49-3/4 19-1/8 151.26
401-200F 20 18-1/4 15-1/2 28-1/4 25-1/2 56-1/2 21-3/16 206.74
401-240F 24 21-1/8 17-1/2 33-1/8 29-1/2 66-1/4 25-3/8 337.03"""

schedule3 = 80
txt3 = """801-002 1/4 5/16 5/16 31/32 31/32 1-15/16 27/32 .04
801-003 3/8 15/32 15/32 1-1/4 1-1/4 2-1/2 31/32 .06
801-005 1/2 19/32 19/32 1-15/32 1-15/32 2-15/16 1-3/16 .11
801-007 3/4 21/32 21/32 1-11/16 1-11/16 3-13/32 1-13/32 .16
801-010 1 7/8 7/8 2 2 4 1-3/4 .27
801-012 1-1/4 1-1/32 1-1/32 2-9/32 2-9/32 4-19/32 2-3/32 .39
801-015 1-1/2 1-3/16 1-3/16 2-9/32 2-9/32 5-1/8 2-3/8 .52
801-020 2 1-7/16 1-7/16 2-15/16 2-15/16 5-7/8 2-7/8 .80
801-025 2-1/2 1-3/4 1-3/4 3-1/2 3-1/2 7-1/32 3-15/32 1.46
801-030 3 2-1/16 2-1/16 3-31/32 3-31/32 7-15/16 4-5/32 2.16
801-040 4 2-1/2 2-1/2 4-3/4 4-3/4 9-1/2 5-1/4 3.52"""

schedule4 = 80
# I manually removed a line with missing data. That is with values "---".
txt4 = """801-050 5 3-1/8 3-1/8 5-25/32 5-25/32 11-5/8 6-13/32 6.03
801-050F 5 5-1/2 5-1/2 8-1/2 8-1/2 17 6-5/16 13.26
801-060 6 3-25/32 3-25/32 6-13/16 6-13/16 13-5/8 7-5/8 10.78
801-080 8 4-13/16 4-13/16 8-7/8 8-7/8 17-3/4 9-23/32 21.21
801-080F 8 7-5/8 7-5/8 11-7/8 11-7/8 23-3/4 9-5/8 22.84
801-100 10 5-15/16 5-29/32 10-29/32 10-29/32 21-13/16 12-13/16 35.83
801-100F 10 9 9 14-1/4 14-1/4 28-1/2 11-15/16 39.82
801-120 12 6-15/16 6-15/16 12-15/16 12-15/16 25-7/8 14-1/4 54.45
801-120F 12 11-1/4 11-1/4 17-1/2 17-1/2 35 14-1/8 67.13
801-140 14 7-1/32 7-1/32 14-7/32 14-1/32 28-7/16 15-21/32 63.61
801-140F 14 12-1/4 12-1/4 19-1/4 19-1/4 38-1/2 15-1/2 103.37
801-160F 16 13 13 21 21 42 17-11/16 144.87
801-180F 18 13-3/4 13-3/4 22-3/4 22-3/4 45-1/2 19-7/8 182.75
801-200F 20 16-3/8 16-3/8 26-3/8 26-3/8 52-3/4 22-1/16 284.24
801-240F 24 20-1/4 20-1/4 32-1/4 32-1/4 64-1/2 26-7/16 335.00"""


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

def process_text(text, schedule):
    result = ""
    for line in text.splitlines():
        if len(result) == 0:
            result+="["
        else:
            result+=",\n"
        result+="["+process_line(line, schedule)+"]"
    result+="]"
    return result
print(process_text(txt1, schedule1))
print(process_text(txt2, schedule2))
print(process_text(txt3, schedule3))
print(process_text(txt4, schedule4))
