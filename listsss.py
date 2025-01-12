test_list1=[1,2,1,3,5]
test_list2=[1,2,4,3,5]
print("the first list is: "+str(test_list1))
print("the second list is: "+str(test_list2))
test_list1.sort()
test_list2.sort()
if len(test_list1) == len(test_list2):
    print("the two lists are equal")
else:
    print("the two lists are not equal")
def common_data(list1, list2):
    result=0 
    for x in list1:
        for y in list2:
            if x == y:
                result=result+x
    return result
print("the sum is:",common_data(test_list1,test_list2)) 
x=int(input("enternumber to be searched"))
if x in test_list1:
    print("the first list conatines the value")
elif x in test_list2:
    print("the second list conatines the value")
else:
    print("the list has no such value")        
          