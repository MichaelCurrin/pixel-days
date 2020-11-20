"""
Log application.
"""
import csv

from colors import color


MOOD_SCALE = {
    1: 'red',
    2: 'orange',
    3: 'yellow',
    4: 'light green',
    5: 'green',
}

# https://www.w3schools.com/charsets/ref_utf_block.asp
# '■'  # square with border
# '■ '  # square with space
# '◾' '◼' '▩'

# Full block. no gaps horizontally.
# DAY_BLOCK = '█'
# Left 7 8ths block. tall and narrow. gaps horizontally.
DAY_BLOCK = '▉'


with open('data.csv') as f_in:
    reader = csv.reader(f_in)
    days = [day for row in reader for day in row]



for i, value in enumerate(days):
    color_name = MOOD_SCALE[int(value)]

    print(color(DAY_BLOCK, fg=color_name), end="")
    
    if (i+1) % 7 == 0:
        print()
print()
