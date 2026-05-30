def fun(x):
    def fun2(y):
        def fun3(z):
            return fun3
        return fun2
greet  = fun(20)
