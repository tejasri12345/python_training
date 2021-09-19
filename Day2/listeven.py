list1 = map(int,input("Enter space seperated numbers: ").split())
list2 = []
for i in list1:
    if(i%2==0):
        list2.append(i)
print(list2)