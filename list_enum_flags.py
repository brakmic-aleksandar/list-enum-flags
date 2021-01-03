#This script lists all power of 2 enum flags for the passed value.
#arg1 should countain value which should be inspected (decimal and hex formats are supported)
#arg2 is optional argument containing max flag value, default value is 2^64

import sys
import math

def is_power_of_two(val):
    return (val & (val-1) == 0) and val != 0

def read_arg_value(val):
    # if hex
    if val.startswith("0x"): 
        return int(val, 16)
    else: 
        return int(val)

args = sys.argv
value = read_arg_value(args[1])
max_value = 2 ** 63

if len(args) > 2:
    max_value = read_arg_value(args[2])

if not is_power_of_two(max_value):
    raise ValueError('max_value is not power of 2')

current_flag = 1
while current_flag < max_value:
    if (value & current_flag) > 0:
        print(f'{current_flag} hex: {hex(current_flag)} log2: {int(math.log2(current_flag))}')
    current_flag = current_flag * 2