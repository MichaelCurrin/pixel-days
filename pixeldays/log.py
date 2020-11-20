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

PATH = 'data.csv'


def load(path):
    with open(path) as f_in:
        reader = csv.reader(f_in)
        days = [day for row in reader for day in row]

    return days


def to_color(value):
    color_name = MOOD_SCALE[int(value)]

    color_string = color(DAY_BLOCK, fg=color_name)

    return color_string


def main():
    days = load(PATH)

    for i, value in enumerate(days):
        output = to_color(value)
        print(output, end="")

        if (i+1) % 7 == 0:
            print()
    print()


if __name__ == "__main__":
    main()
