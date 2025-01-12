l=["python\n","programming\n","language\n"]
file1=open('myfile.txt','w')
file1.writelines(l)
file1.close()
file1=open('myfile.txt','r')
lines=file1.readlines()
count=0
for line in lines:
    count+=1
    print("lines{}:{}".format(count,line.strip()))
