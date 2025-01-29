menu={}
while True:
    key=input("Enter the product name enter q to exit:")
    if key=='q' or key=='Q' :
        break
    value=input("Enter the product price:")
    menu[key]=value

print(menu)
while True: 
        check=input("enter the item you want to find in the dictionary enter q to quit:")
        if check in menu:
            print("Item found {check}:{menu[check]}")
        if check=='q' or check== 'Q':
            break
        elif not check in menu:
            print("ITEM NOT FOUND")
        
