import threading

class Task:
    def __init__(self,fnTarget,*args,**kwargs):
        self._target=fnTarget
        self._args=args
        self._kwargs=kwargs
        self._result=None
        self._thread=threading.Thread(target=lambda:self._run())
        self._thread.start()

    def _run(self):
        self._result=self._target(*self._args,**self._kwargs)

    @property
    def result(self):
        if self._thread.is_alive():
            self._thread.join()

        return self._result


    def wait(self):
        self._thread.join()



def asynchronous(fn):
    def wrapper(*args,**kwargs):
        task=Task(fn,*args,**kwargs)
        return task

    return wrapper