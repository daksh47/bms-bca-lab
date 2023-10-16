#sum of digits without using loop
a=int(input("Enter the value of a "))
b=a%10
a=a/10
c=a%10
a=a/10
d=a%10
a=a/10
e=a%10
sum=int(b+c+d+e)
print("Addition is",sum)
