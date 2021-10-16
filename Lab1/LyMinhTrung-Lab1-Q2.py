import math

a = int(input("Enter the Private Key Selected for Alice: "))
b = int(input("Enter the Private Key Selected for Bobs: "))
g = int(input("Enter the Public Keys available G: "))
p = int(input("Enter the Public Keys available P (prime number): "))
#general key
x = int(pow(g,a,p))
y = int(pow(g,b,p))
#key of Alice
kA = int(pow(y,a,p))
#key of Bo
kB = int(pow(x,b,p))
print("The private key for Alice: ", a)
print("The private key for Bobs: ", b)
print("The general key: ", x)
print("The secret key for Alice: ", kA)
print("The secret key for Bobs: ", kB)