list1 = map(int,input("Enter space seperated values: ").split())
list2 = []
for i in list1:
    if(i>10 and i<50):
        square = i*i
        list2.append(square)
print(list2)
