from collections import defaultdict

class Event:
    def __init__(self):
        self.handlers = defaultdict(list)

    def on(self, evt_name, handler):
        self.handlers[evt_name].append(handler)
        return self
    
    def emit(self, evt_name, *args, **kwargs):
        if evt_name not in self.handlers: return False

        for handler in self.handlers[evt_name]:
            handler(*args, **kwargs)


