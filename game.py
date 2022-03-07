import random
print(".......SNAKE/WATER/GUN.......")
def chosen(comp,user):
    r=True
    if comp=="s":
        if user=="g":
            return r
        elif user=="w":
            r=False
            return r
        else:
            return None
    elif comp=="g":
        if user=="s":
            r=False
            return r
        elif user=="w":
            return r
        else:
            return None
    elif comp=="w":
        if user=="s":
            return r
        elif user=="g":
            r=False
            return r
        else:
            return None

print("Choose your option")
print("'s' for snake")
print("'g' for gun")
print("'w' for water:")
user=input()
compScore=random.randint(1,3)
if compScore==1:
    comp= "s"
elif compScore==2:
    comp= "g"
elif compScore==3:
    comp="w"
print("computer chose :"+comp)
if user=="s" or user=="g" or user=="w":
     a= chosen(comp,user)
     if a==None:
        print("Game tie🤗")
     elif a==True:
        print("U win🥳🥳")
     elif a==False:
        print("U lose!🙄")
else:
     print("input is invalid")



