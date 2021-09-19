string = input("Enter string: ")
a=0
e=0
i=0
o=0
u=0
for char in string:
    
    if 'a' == char or 'A' == char:
        a +=1
    if 'e' == char or 'E' == char:
        e +=1
    if 'i' == char or 'I' == char:
        i +=1
    if 'o' == char or 'O' == char:
        o +=1
    if 'u' == char or 'U' == char:
        u +=1
print("a vowel count is: ", a)
print("e vowel count is: ",e)
print("i vowel count is: ",i)
print("o vowel count is: ",o)
print("u vowel count is: ",u)