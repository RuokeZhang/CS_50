expression=input("Expression: ")
x, y, z = expression.split(" ")
a=int(x)
b=int(z)
#turn int to float
res=eval(f"{a}{y}{b}")
print(f"{res:.1f}")
