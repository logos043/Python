# house.py

class HousePark:
    lastname = "박"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졋네"  % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))



class HouseKim(HousePark):
    lastname = "김"
    def travel(self,where, day ):
        print(self.fullname, where, day)



pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet
