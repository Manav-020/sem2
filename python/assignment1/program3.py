b=float(input("enter length in feet:"))
c=0
#while b!=8:
print(" enter 1 to get length in inch\n","enter 2 to get length in yards\n","enter 3 to get length in miles\n","enter 4 to get length in milliemters\n","enter 5 to get length in centimeters\n","enter 6 to get length in meters\n","enter 7 to get length in kilometers\n","enter 8 to get length in exit\n")
n=int(input("enter number:"))
z=[b*12,b*(0.33),b*(0.000189),b*(304.8),b*(30.48),b*(0.3048),b*(0.0003048)]
match n:
    case 1:print("length in inch is",z[0])
    case 2:print("length in yards is",z[1])
    case 3:print("length in miles is",z[2])
    case 4:print("length in millimeters is",z[3])
    case 5:print("length in centimeters is",z[4])
    case 6:print("length in meters is",z[5])
    case 7:print("length in kilometers is",z[6])
    case _:print("invalid")