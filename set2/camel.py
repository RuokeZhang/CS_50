camel=input("camelCase: ")
snake=""
for c in camel:
    if c.islower():
        snake+=c
    else:
        snake+='_'+c.lower()
print(snake)
