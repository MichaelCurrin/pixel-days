"""
Based on
    https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
"""


class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


print(bcolors.OKBLUE, 'text', bcolors.ENDC)
