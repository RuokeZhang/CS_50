s=input("Input: ")
s1=""
for c1 in s:
    c=c1.lower()
    if not (c=='a' or c=='i' or c=='u' or c=='e'or c=='o'):
        s1+=c1
print(s1)