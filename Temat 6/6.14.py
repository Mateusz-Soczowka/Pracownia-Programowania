arr=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
longest=""
for x in range(0,len(arr)):
    if len(arr[x])>len(longest):
        longest=arr[x]
        
print(f"Longest name: {longest}")