list1 = input("Enter space seperated values: ").split()
list2 = input("Enter space seperated values: ").split()
merged_list = [(list2[i], list1[i]) for i in range(0, len(list1))]
print(merged_list)