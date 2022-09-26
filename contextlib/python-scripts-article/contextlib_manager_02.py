from contextlib import contextmanager


@contextmanager
def single():
    print('Yielding')
    yield
    print('Exiting context manager')


context = single()
with context:
    pass

# Yielding
# Exiting context manager

with context:
    pass

# Traceback (most recent call last):
#    Python Shell, prompt 9, line 1
#    File "/usr/local/lib/python3.5/contextlib.py", line 61, in __enter__
#       raise RuntimeError("generator didn't yield") from None
# builtins.RuntimeError: generator didn't yield