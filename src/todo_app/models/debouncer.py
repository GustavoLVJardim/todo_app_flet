import threading

class Debouncer:
    def __init__(self, delay_seconds=0.3):
        self.delay = delay_seconds
        self.timer = None

    def debounce(self, func, *args, **kwargs):
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.delay, func, args, kwargs)
        self.timer.start()
