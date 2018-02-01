def fun():
    print("I am in fun()")

    def lfun():  # function inside a function
        print("I am in Local Function")

    lfun()


fun()
