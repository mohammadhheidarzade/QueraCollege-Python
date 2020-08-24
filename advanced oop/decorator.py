def decorator(validator):
    def fun(funct):
        def ret(*args):
            if validator(*args):
                return funct(*args)
            else:
                return "error"
        return ret
    return fun