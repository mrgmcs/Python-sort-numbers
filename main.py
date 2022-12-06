cnt = int(input("enter number of itemts: "))
lst = []
for i in range(cnt):
    newItem = int(input("enter your item: "))
    lst.append(newItem)
print("sotrting")
new_lst = []
print(lst)

def checklist(flist):
    global min1
    min1=flist[0]
    for i in range(1,len(flist)):
        if(flist[i]<min1):
            min1=flist[i]
    return min1

while lst!=[]:
    for i in lst:
        #check min
        if checklist(lst)==i:
            new_lst.append(i)
            lst.remove(i)
        
print("sorted list is :",new_lst)
print("old list is: ",lst)