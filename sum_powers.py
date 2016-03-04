user_input= raw_input("Enter a number here: ")
b = float(user_input)
while b == 1:
    user_input = raw_input("Number can not be equal to one. Enter a number here: ")
    b=float(user_input)

n_str = raw_input ("Enter a natural number: ")
n= int(n_str)
while n < 0:
    n_str = raw_input ("A natural number must have a value greater than zero. Enter a natural number: ")
    n= int(n_str)


x = 0
y = 0

while y <= n:
    x += b**(y)
    y += 1

print x

print (b**(n+1)-1)/(b-1)
