import sys

path = '/path/to/text.txt'

with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)

# ----------------------------


from contextlib import redirect_stdout

path = '/path/to/text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)
