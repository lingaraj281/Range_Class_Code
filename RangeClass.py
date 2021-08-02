
# RANGE CLASS CODE PROBLEM - THE UPLIFT PROJECT
class Range():
    def __init__(self, n2, n1=0):
        self.n1 = n1
        self.n2 = n2
        self.data = list(range(self.n1, self.n2))

    def show(self):
        print(self.data)

    def contains(self, n3, n4):
        self.n3 = n3
        self.n4 = n4
        self.data1 = list(range(self.n3, self.n4))
        for a in self.data1:
            if a in self.data:
                c = True
            else:
                c = False
                break
        print(c)

    def overlaps(self, n12, n13):
        self.n12 = n12
        self.n13 = n13
        self.data6 = list(range(self.n12, self.n13))
        for a in self.data1:
            if a in self.data:
                c = True
            else:
                c = False
                break
        print(c)

    def disjoint(self, n5, n6):
        self.n6 = n6
        self.n5 = n5
        self.data2 = list(range(self.n5, self.n6))
        for a in self.data2:
            if a in self.data:
                c = "False"
                break
            else:
                c = "True"
        print(c)

    def touching(self, n7, n8):
        self.n7 = n7
        self.n8 = n8
        self.data3 = list(range(self.n7, self.n8))
        if (self.data[0] == self.data3[-1]) or (self.data[-1] == self.data3[0]):
            print("True")
        else:
            print("False")

    # True if the length of the super range is less than the length of the sub range
    def lessThan(self, n8, n9):
        self.n8 = n8
        self.n9 = n9
        self.data4 = list(range(self.n8, self.n9))
        if len(self.data) < len(self.data4):
            print("True")
        else:
            print("False")

    # True if first member of superrange is lessthan first member of sub range
    def lessThan2(self, n10, n11):
        self.n10 = n10
        self.n11 = n11
        self.data5 = list(range(self.n10, self.n11))
        if self.data[0] < self.data5[0]:
            print("True")
        else:
            print("False")


e = Range(n1=4, n2=9)
f = Range(4)

e.contains(3, 4)
f.contains(3, 4)

e.overlaps(3, 4)
f.overlaps(3, 4)

e.disjoint(3, 4)
f.disjoint(3, 4)

e.touching(3, 4)
f.touching(3, 4)

e.lessThan(3, 4)
f.lessThan(3, 4)

e.lessThan2(3, 4)
f.lessThan2(3, 4)
