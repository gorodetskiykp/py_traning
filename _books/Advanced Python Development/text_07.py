from concurrent.futures import ThreadPoolExecutor


def helloworld():
    print("Hello world!")


with ThreadPoolExecutor() as pool:
    pool.submit(helloworld)


def calculate():
    return 2**16


with ThreadPoolExecutor() as pool:
    task = pool.submit(calculate)


print(task.result())