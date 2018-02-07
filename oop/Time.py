class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def __str__(self):
        return "%d:%d:%d" % (self.__hh, self.__mm, self.__ss)

    def in_seconds(self):
        return self.__hh * 60 * 60 + self.__mm * 60 + self.__ss

    def __gt__(self, other):
        return self.in_seconds() > other.in_seconds()

    def __eq__(self, other):
        return self.in_seconds() == other.in_seconds()

    def __add__(self, other):
        seconds = self.in_seconds()
        totalsecs = seconds + other

        hours = totalsecs / 3600;
        minutes = (totalsecs % 3600) / 60;
        seconds = totalsecs % 60;

        return Time(hours,minutes,seconds)


t1 = Time(10, 30, 20)
print(t1)
print(t1.in_seconds())

t2 = Time(11, 30, 20)
print(t2)
print(t2.in_seconds())

t3 = Time(10, 30, 20)
print(t3)
print(t3.in_seconds())

print(t1 != t3)
print(t1 < t2)
print(t1 + 70)