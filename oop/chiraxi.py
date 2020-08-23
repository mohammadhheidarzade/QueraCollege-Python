class ExceptionProxy(Exception):
    pass

def transform_exceptions(func_ls):
    res = []
    for func in func_ls:
        try:
            func()
        except Exception as err:
            e = ExceptionProxy()
            e.msg = str(err)
            e.function = func
        else:
            e = ExceptionProxy()
            e.msg = "ok!"
            e.function = func
        res.append(e)
    return res