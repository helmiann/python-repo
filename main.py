
def area (dimension1,dimension2,shape="triangle"):
    if shape == "rectangle":
    #base is length height is width
        total = dimension1*dimension2
    elif shape == "triangle":
        total = (1/2)*dimension1*dimension2
    else:
        print("hanya bisa rectangle dan triangle")
        return None
    return total

def loop (n):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)

p = str(input("masukkan operasi apa yang anda ingin lakukan : "))
if p == "menghitung":
    x=str(input("masukkan bentuk bangun yang ingin dihitung : "))
    y=int(input("masukkan panjangnnya : "))
    z=int(input("masukkan lebarnya : "))
    c=area(z,y,x)
    print(c)
    if c is not None:
        print(f"Luas {x} adalah {c}")
else:
    y=int(input("masukkan angka yang ingin diputar : "))
    print(loop(y))

     

i = 5       
for x in range(i):
        x+=1
        print ("*"*x)