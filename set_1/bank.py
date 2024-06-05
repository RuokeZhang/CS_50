s=input("Greeting: ")
if "hello" in s.lower():
    print("$0")
elif s.lower().startswith("h"):
    print("$20")
else:
    print("$100")