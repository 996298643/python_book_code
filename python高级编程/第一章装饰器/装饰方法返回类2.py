class Task(object):

    def __call__(self, *args, **kwargs):
        self.run(self, *args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError("")

    def identify(self):
        print("I am a task")

def task(decorated):

    class SubClassTask(Task):
        def run(self, *args, **kwargs):
           return decorated(*args, **kwargs)

    return SubClassTask


@task
def foo():
    return 2+2

print(foo().run())

print(foo().identify())