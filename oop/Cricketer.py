# multiple inheritance: calling init of multiple base classes


class Bowler:
    def __init__(self, name, wickets=0):
        self._name = name
        self._wickets = wickets

    def __str__(self):
        return "%s %d" % (self._name, self._wickets)


class Batsman:
    def __init__(self, name, runs=0):
        self._name = name
        self._runs = runs

    def __str__(self):
        return "%s %d" % (self._name, self._runs)


class AllRounder(Batsman, Bowler):
    def __init__(self, name, runs, wickets):
        Batsman.__init__(self, name, runs) #using base class name to call init. Notice that we send the 'self' as a parameter
        Bowler.__init__(self, name, wickets)

    def __str__(self):
        return "%s %d %d" % (self._name, self._runs, self._wickets)


c = AllRounder("Abc", 20000, 500)
print(c)
print(dir(c)) # 'name' variable will only be once for AllRounder
