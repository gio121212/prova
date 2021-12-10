import functions

a = float(input("Enter a real number: "))
b = float(input("Enter a real number (not zero): "))

print(
"+ ------>" , functions.sum(a,b),
"\n* ------>" , functions.multiply(a,b),
"\n/ ------>" , functions.divide(a,b),
"\nmodulo ------>" , functions.mod(a,b),
"\nsquared ------>", a ,"^ 2 =" , functions.sq(a), "and", b ,"^ 2 =" , functions.sq(b))