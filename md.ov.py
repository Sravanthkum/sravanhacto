class A_class:
    def m1(self, *args):
        if len(args) == 0:
            print("0's number of arguments")
        elif len(args) == 1:
            print("1's number of arguments")
        elif len(args) == 2:
            print("2's number of arguments")
        elif len(args) == 3:
            print("3's number of arguments")
        else:
            print("Too many arguments")

a1 = A_class()
a1.m1()
print()
a1.m1(1000)
print()
a1.m1(1000, 2000)
print()
a1.m1(1000, 2000, 3000)
