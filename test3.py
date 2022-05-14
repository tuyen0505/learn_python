class Person:
    def __format__(self, str) :
        print(str)
        return "sdhfdhghdg"
    def name(self,a,b):
        print(a,b)
        return "dfsgdf"
tuyen=Person()
print(format(tuyen,"fkgh"),"\n",tuyen.name(3,4))
