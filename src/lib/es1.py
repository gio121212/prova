import functions

a = float(input("Enter a real number: "))
b = float(input("Enter a real number: "))

print("+ ------>" , functions.sum(a,b))
print("* ------>" , functions.multiply(a,b))
print("/ ------>" , functions.divide(a,b))
print("modulo ------>" , functions.mod(a,b))
print("squared ------>", a ,"^ 2 =" , functions.sq(a), "and", b ,"^ 2 =" , functions.sq(b))