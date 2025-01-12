from graphics.rectangle.import*
from graphics.circle.import*
print("enter choice")
print("1.area of rectangle")
print("2.perimeter of rectangle")
print("3.area of cuboid")
print("4.perimeter of cuboid")
print("5.area of circle")
print("6.circumference of circle")
print("7.area OF sphere")
print("8.exit")
choice=int(input("enter your choice:"))
if choice==1:
    f=float(input("enter length"))
    b=float(input("enter breadth"))
    print("area=",calc.area(f,b))
elif choice==2:
    f=float(input("enter length"))
    b=float(input("enter breadth"))
    print("Perimeter=",calc.perim(f,b))
elif(choice==3)or(choice==4):
    l=float(input("enter length"))
    b=float(input("enter breadth"))
    h=float(input("enter height"))
    if choice==3:
        print("area=",calc.area_lub(l,b,h))
    else:
        print("perimeter=",calc.perim_lub(l,b,h))
elif(choice==5)or(choice==6):
    r=float(input("enter radius"))
    if choice==5:
        print("area=",calc.areacircle(r))
    else:
        print("area=",calc_perimcicle(r))    
    break:
elif choice==7:
    r=float(input("enter radius"))
    print("area=",calc.areasphere(r))
elif choice==8:
    print("program exited")
else:
    print("invalid choice")