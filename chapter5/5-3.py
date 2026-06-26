class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second 
        return result
    def sub(self):
        result = self.first - self.second 
        return result
    def mul(self):
        result = self.first * self.second 
        return result
    def div(self):
        result = self.first / self.second
        return result
    

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(MoreFourCal):
    def div(self):
        if self.second == 0:
            result = 0
        else:
            result = self.first / self.second
        return result

a=SafeFourCal(3,0)


# a.setdata(3,4)
# b.setdata(5,0)


# print(a.first)
# print(a.second)
print("add : "+str(a.add()))
print("sub : "+str(a.sub()))
print("mul : "+str(a.mul()))
print("div : "+str(a.div()))
print("pow : "+str(a.pow()))

# print(b.first)
# print(b.second)
# print(b.add())