
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
        # if (self.data3[-1] + 1 == self.data[0]) or [self.data[-1] + 1 == self.data3[0]]:
        #     print("True")
        # else:
        #     print("False")
        print(self.data3[-1] + 1 == self.data[0])

    # True if the length of the super range is less than the length of the sub range

    def lessThan(self, n8, n9):
        self.n8 = n8
        self.n9 = n9
        self.data4 = list(range(self.n8, self.n9))
        if len(self.data) > len(self.data4) and self.data4[0] > self.data[0]:
            print("True")
        else:
            print("False")


r1 = Range(n1=4, n2=9)
r2 = Range(4)

r1.contains(3, 4)
r2.contains(3, 4)

r1.overlaps(3, 4)
r2.overlaps(3, 4)

r1.disjoint(3, 4)
r2.disjoint(3, 4)


r1.touching(3, 4)
r2.touching(3, 4)


r1.lessThan(3, 4)
r2.lessThan(3, 4)
