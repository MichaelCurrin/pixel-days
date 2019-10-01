import csv

from colors import color

with open('data.csv') as f_in:
    reader = csv.reader(f_in)
    days = [day for row in reader for day in row]


COLOR_MAP = {
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
# SQUARE = '█'
# Left 7 8ths block. tall and narrow. gaps horizontally.
SQUARE = '▉'

for i, value in enumerate(days):
    c = COLOR_MAP[int(value)]

    print(color(SQUARE, fg=c), end="")
    if (i+1) % 7 == 0:
        print()
print()
