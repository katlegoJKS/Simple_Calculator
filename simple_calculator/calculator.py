class Calculator:

    def __init__(self):
        pass

    #An add function that adds two or multiple integers
    def add(self,*args):                #we use '*args' to pass as many arguments as required
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

print("---Add Function---")
print(add1.add(1,2,3,4,5))
print(add1.add(1,2))
print(add1.add(-1,-1))

product1 = Calculator()

print("\n---Multiply Function---")
print(product1.multiply(1,3))
print(product1.multiply(-1,3))
print(product1.multiply(1,2,3,4,5))