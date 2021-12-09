x=str(input("Enter the PIN code: "))

pin="0805"

tries=0

while x!=pin and tries<2:
    tries=tries+1
    print("Incorrect...")
    x=str(input("Enter the PIN code: "))
    
if x==pin:
    print("Correct")
    
else:
    print("Inorrect...")
    print("Sorry, your payment card has been blocked.")