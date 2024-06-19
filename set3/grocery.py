dict={
}
while True:
    try:
        item=input().upper()
        if item in dict:
            dict[item]+=1
        else:
            dict[item]=1
    except EOFError:
        break
    
# sorted applies to a list
for item, count in sorted(dict.items()):
    print(f"{count} {item}")