#Question-1-i want to get 10 when  to calculate 2 numbers
lst=[2,3,12,5,6,4,9]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==10:
            print(lst[i],lst[j])
#time complexity is O(n^2)
#space complexity is O(1)

sett=set()
t=10
for i in lst:
    l=i
    val=t-l
    if val in sett:
        print(val,i)
    else:
        sett.add(i)
    
#time complexity is O(n)
#space complexity is O(n)




#Question-2-i want to move all 6 in the end
lst=[6,6,6,4,5,66,6,5,8,6,9,6,3,5,9,6]
for i in range(len(lst)-1):
    for j in range(len(lst)-1,i,-1):
        if lst[i]==6 and lst[j]!=6:
            lst[j],lst[i]=lst[i],lst[j]
print(lst)

#time complexity O(n^2)
#space complexity O(1)
lst=[6,6,6,4,5,66,6,5,8,6,9,6,3,5,9,6]
lst6=[]
nwlst=[]
for i in lst:
    if i==6:
        lst6.append(i)
    else:
        nwlst.append(i)
else:
    lst=nwlst+lst6
print(lst)

#time complexity O(n)
#space complexity O(n)

