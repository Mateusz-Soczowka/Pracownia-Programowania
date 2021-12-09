arr=[4,36,12,28,9,44,5]
arr2=[5,1,36]
for x in arr:
    appear=False
    for y in arr2:
        if x==y:
            appear=True
    if appear==False:
        print(x)