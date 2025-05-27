def check(func):
    def isZero(a, b):
        if b == 0:
            return
        return func(a, b)
    return isZero
@check
def div(a, b):
    return a / b
print(div(6, 2))
print(div(6, 0))
