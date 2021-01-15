class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        x=len(self.__elements)
        self.maximumDifference=0
        for i in range(x-1):
            for j in range(x):
                diff=abs(self.__elements[j]-self.__elements[i])
                if diff>self.maximumDifference:
                    self.maximumDifference=diff
        
    


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)