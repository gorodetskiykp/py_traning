import threading


def helloworld():
    print("Hello world!")


thread = threading.Thread(
    target=helloworld,
    name='helloworld',
)
thread.start()
thread.join()


class HelloWorldThread(threading.Thread):
    def run(self):
        print("Hello world!")


thread = HelloWorldThread(name='helloworld')
thread.start()
thread.join()
