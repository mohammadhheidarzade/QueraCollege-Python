class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = ""
        self.calls = dict()
    def last_invoked_method(self):
        if self.last_invoked == "":
            raise Exception("No Method Is Invoked")
        return self.last_invoked
    def count_of_calls(self, method_name):
        return self.calls.get(str(method_name) , 0)    
    def was_called(self, method_name):
        return bool(self.count_of_calls(method_name))
    def __getattr__(self, name):
        if name in dir(self._obj):
            self.last_invoked = name
            self.calls[name] = self.calls.get(name,0) + 1
            return getattr(self._obj, name)
        else:
            raise Exception("No Such Method")