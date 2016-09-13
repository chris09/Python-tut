class me:
    def __init__(self, foo):
        self.myvar = foo

    def getval(self):
        return self.myvar

me = me('this')
x = me.getval()
print(x)
