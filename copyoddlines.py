fn=open('bcd.txt','r')
fn1=open('nfile.txt','w')
cnt=fn.readlines()
type(cnt)
for i in range(0,len(cnt)):
    if(i%2==0):
        fn1.write(cnt[i])
    else:
        pass
fn1.close()
fn1=open('nfile.txt','r')
cnt1=fn1.read()
print(cnt1)
fn.close()
fn1.close()
