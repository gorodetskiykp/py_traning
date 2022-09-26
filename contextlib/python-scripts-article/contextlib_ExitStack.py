from contextlib import ExitStack

with ExitStack as stack:
    file_objects = [
        stack.enter_context(open(fname)) for filename in filenames
    ]