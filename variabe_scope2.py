gv = "Global Variable"

def fun():
    print("I am in fun()")
    ev = "Enclosing Variable"

    def lfun():  # function inside a function
        lv = "Local Variable"
        #nonlocal ev # informing interpreter that we want to use the enclosing scoped variable
        ev = "Modifing Enclosing Variable" # if not specified with nonlocal keyword, this does not modify the 'ev' in fun(). It creates a new variable inside lfun()
        print("I am in Local Function")
        print(gv,",",ev,",",lv)

    lfun()
    print(ev)


fun()
