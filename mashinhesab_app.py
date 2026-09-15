# import ... 
import time


# functions ...

def add(a,b):
    return a+b

def menha(a,b):
    return a-b

def zarb(a,b):
    return a*b

def taghsim(a,b):
    return a/b

def bakhpaziri(a,b):
    if a%b == 0:
        print(f"adad {a} bar {b} bakhshpazir ast.")
    else:
        print("bakhpazir nist")


#mantegh barname asli

while True:
    print("-----------------///////////////-----------------")
    print("in barname yek mashin hesab sade ast ke bakhshpaziri 2adad ra ham elam mikonad yeki az adad ra entekhab konid:")
    print("1=jam adad   2=zarb adad     3=taghsim adad      4=menha adad    5=bakhpaziri    6=khoroj")
    #print("lotfan adad aval va adad dovom ro vared konid")
    print("********************************************************************************")
    entekhab_karbar = int(input("**gozine ra vared konid** : "))

    if entekhab_karbar==1:
        adad_1 = float(input("adad aval = "))
        adad_2 = float(input("adad dovom = "))
        print(add(adad_1,adad_2))

    if entekhab_karbar==2:
        adad_1 = float(input("adad aval = "))
        adad_2 = float(input("adad dovom = "))
        print(zarb(adad_1,adad_2))

    if entekhab_karbar==3:
        adad_1 = float(input("adad aval = "))
        adad_2 = float(input("adad dovom = "))
        print(taghsim(adad_1,adad_2))

    if entekhab_karbar==4:
        adad_1 = float(input("adad aval = "))
        adad_2 = float(input("adad dovom = "))
        print(menha(adad_1,adad_2))

    if entekhab_karbar==5:
        adad_1 = float(input("adad aval = "))
        adad_2 = float(input("adad dovom = "))
        bakhpaziri(adad_1,adad_2)

    if entekhab_karbar==6:
        print("paian barname")
        time.sleep(5)
        break