type=input("File name: ")
type=type.lower()

if type.find(".gif") is not -1:
    print("image/gif")
elif type.find(".jp") is not -1:
    print("image/jpeg")
elif type.find(".png") is not -1:
    print("image/png")
elif type.find(".pdf") is not -1:
    print("application/pdf")
elif type.find(".txt") is not -1:
    print("text/plain")
elif type.find(".zip") is not -1:
    print("application/zip")
else:
    print("application/octet-stream")