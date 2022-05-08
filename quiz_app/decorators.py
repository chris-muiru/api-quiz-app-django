
def checkDuplicates(func):
    def wrapper(*args,**kwargs):
        # conditions
        return func(*args,**kwargs)
    return wrapper