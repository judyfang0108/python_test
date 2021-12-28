class FooBar():
    def __init__(self, n):
        self.n = n

    def foo(self):
        for _ in range(self.n):
            print("foo")

    def bar(self):
        for _ in range(self.n):
	        print("bar")
    
    def yeah(self):
        for _ in range(self.n):
	        print("yeah")

    def all(self):
        for _ in range(self.n):
	        print("foobaryeah")

if __name__ == '__main__':
    n=int(input('Input: n = '))
    a=FooBar(n)
    print('Output:')
    a.all()