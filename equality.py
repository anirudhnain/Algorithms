class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return f"C({self.x})"
    def __hash__(self):
        print ("hash:",hash(self.x))
        return hash(tuple([self.x]))
    def __eq__(self, other):
        print (self.x,other.x)
        return (
            self.__class__ == other.__class__ and
            self.x == other.x
        )
d = dict()
c = C(1)
d[c] = 42
print (d)
print (c in d)  # c is in both!
c.x = 1
print ("Newx:",c.x)
print(c in d)   # c is in neither!?
for key in d.keys():
    print ("Hash key:",hash(key.x))