def add(str1):
    length=len(str1)
    if length>2:
       if str1[-3: ]=='ing':
          str1+='ly'
       else:  
          str1+='ing'
       return str1
print(add(input("Enter Strings:")))
