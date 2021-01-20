class C1:
    def sum(self,a,b):
        return (a+b)

obj = C1()
num1 = eval(input('Enter A: '))
num2 = eval(input('Enter B: '))
print(obj.sum(num1, num2))
