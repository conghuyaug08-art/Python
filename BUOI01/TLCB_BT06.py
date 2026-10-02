a = (int)(input("Nhap a: "))
b = (int)(input("Nhap b: "))
c = (int)(input("Nhap c: "))

if (a>=b and a>=c):
    max = a
elif (b>= a and b >= c):
    max = b
else:
    max = c
if (a<=b and a<=c):
    min = a
elif (b<=a and b<=c):
    min = b
else:
    min = c
    
print("So lon nhat: ", max)
print("So nho nhat: ",  min)
    
    
    
    

