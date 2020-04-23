class Calculator:

    def __init__(self):
        pass

    def add(self,*args):
        result = 0
        for number in args:             
            value = int(number)
            result += value
        return result

    def multiply(self,*args):
        product = 1
        for number in args:
            value = int(number)
            product *= value
        return product

add1 = Calculator()

print(add1.add(1,2,3,4,5))
print(add1.add(1,2))
print(add1.add(-1,-1))

product1 = Calculator()

print(product1.multiply(1,3))
print(product1.multiply(-1,3))
print(product1.multiply(1,2,3,4,5))

if __name__=='__main__':
    Calculator()