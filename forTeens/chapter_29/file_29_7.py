class JustAClass:
    def foo1(self):
        print("foo1 was called")
        self.foo2()     #Call foo2() using dot notation

    def foo2(self):
        print("foo2 was called")

#Main code starts here
x = JustAClass()
x.foo1()    #Call foo1() which, in turn, will call foo2()
