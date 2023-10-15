type=input("File name: ")

if type.find(".gif")>-1:
    print("image/gif")
elif type.find(".jpg")>-1:
    print("image/jpg")
elif type.find(".jpeg")>-1:
    print("image/jpeg")
elif type.find(".png")>-1:
    print("image/png")
elif type.find(".pdf")>-1:
    print("application/pdf")
elif type.find(".txt")>-1:
    print("text/plain")
elif type.find(".zip")>-1:
    print("application/zip")
else:
    print("application/octet-stream")