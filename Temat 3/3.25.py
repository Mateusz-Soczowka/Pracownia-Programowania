x=int(input("x: "))
y=int(input("y: "))
for a in range(1,x+1):
    word=""
    for b in range(1,y+1):
        if a==1 or b==1 or a==x or b==y:
            word=word+"*"
        else:
            word=word+" "
    print(word)