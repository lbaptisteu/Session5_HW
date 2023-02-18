try:
    a = int(input("Tell me the closes approximation of your gross salary"))
    b = int(input("Tell me the number of children you have"))
    tax = 1

except ValueError:
    print("One of the provided values was invalid")



if  a > 4000:
    tax += 18
elif 2000 < a < 4000:
    tax += 14
elif 1000 < a < 2000:
    tax += 12
else:
    tax += 10


try:
    tax -=b
    if a > 2000:
        b *=0.5
    else:
        b *=1
finally:
    tax -=1
    print("Your approximate net salary is", a%tax)





