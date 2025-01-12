
n=int(input("enter the limits:"))
first=0
second=1
print("fibonacci series of ",n,"is.....")
print(first)
print(second)
for i in range(2,n):
      third=first+second
      print(third)
      first=second
      second=third
