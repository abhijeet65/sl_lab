import re
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
l1=["No1","Iam2", "notcolorblind3","myworld4 ","isblackandwhite5","trytokeep6"]
l=["No 1","Iam 2", "notcolorblind 3","myworld 4 ","isblackandwhite 5","trytokeep 6"]
for i in range(len(l)):
	if i%2 != 0:
		print(l[i])
for i in range(1,len(l)):
	if (i+1)%3==0:
		l[i]=l[i].upper()
		print(l[i])
l2=[reverse(i) for i in l]
print(l2)
#extracting numbers from list with space as de-limiter
l3=[item for subitem in l for item in subitem.split() if item.isdigit()]
print(l3)
#extracting numbers from list without a delimiter
l4=[ re.findall('\d+', i) for i in l1]
#returns a list for each string
print(l4)
