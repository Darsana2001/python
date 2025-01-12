a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
i=1
while(i<=a and i<=b):
	if(a%i==0 and b%i==0):
		gcd=i
	i=i+1
print("gcd of the number is",gcd)

