name=input("File name: ")
fName=name.strip()
if fName.lower().endswith(".jpg"):
    print("image/jpeg")
elif fName.lower().endswith(".gif"):
    print("image/gif")
elif fName.lower().endswith(".jpeg"):
    print("image/jpeg")
elif fName.lower().endswith(".png"):
    print("image/png")
elif fName.lower().endswith(".pdf"):
    print("application/pdf")
elif fName.lower().endswith(".txt"):
    print("text/plain")
elif fName.lower().endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")


