string = input("Enter a string: ")
vowel = 0
consonent = 0
for i in string:
    
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel +=1
    else:
        consonent+=1

print("number of vowels in a string: ",vowel)
print("number of consonents in a string: ",consonent)