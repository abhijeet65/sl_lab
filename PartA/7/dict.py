atom = {"H":1 ,"Li":3,"Mg":12,"Ca":20,"Sr":38,"Ba":56,"Be":4}
#Entering from user
key=input("Enter atomic symbol")
value=input("Enter atomic number")
atom[key]=value
print(atom)
#duplicate elements not repeated
print("no of elements in dic is " + str(len(atom)))
#dictionary search wrt key
s=input("Enter atomic symbol to be searched")
if s in atom:
	print("Symbol: " + s)
	print("A.no:" + str(atom[s]))
else:
	print("Entered element absent in dictionary")	
   	 
