with open('fauxfile.txt') as fobj:
    for line in fobj:
        print(line)

# Traceback (most recent call last):
#     Python Shell, prompt 4, line 1
# builtins.FileNotFoundError: [Errno 2] No such file or directory: 'fauxfile.txt'


from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)