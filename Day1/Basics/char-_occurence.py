string = input("Enter a string:")
char  = input("Enter a charecter you want to count in above  string: ")
count = 0
for i in string:
    if char == i:
        count+=1
print(count)