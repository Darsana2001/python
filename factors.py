number=36
factors=[]
for i in range(1,int(number**0.5)+1):
    if number%i==0:
        factors.append(i)
        if i!=number//i:
            factors.append(number//i)
factors.sort()
print(factors)