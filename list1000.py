#Jack Lawrence
#Programming PM
#1/23/2018
namelist = ['Jack', 'Jim','Joe','Joel','Josh']
def newlistcreate(namelist):
    x=0
    while x==0:
        z = input("Add a new name ").title()
        namelist.append(z)
        y = input("Would you like to add another?[Y/N] ").upper()
        print("")
        if y!="Y":
            print("Heres the new list")
            print("")
            return namelist
            x=1
       
    
        
final_z = newlistcreate(namelist)

print(final_z)
