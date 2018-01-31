g = "global"  # global scope


def fun():
    l = "local"  # local scope
    print(l, g)


def fun2():
    global g  # informing interpreter that we want to use the global variable
    g = "changed in fun2"  # if not pointed to global; creates a new variable in local scope
    print(g)


fun2()
fun()
