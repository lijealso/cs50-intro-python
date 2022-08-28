answer = input("File name: ").strip().upper().split(".")

ext = answer[-1]

if ext == "GIF":
    print("image/gif")
elif ext == "JPG" or ext == "JPEG":
    print("image/jpeg")
elif ext == "PNG":
    print("image/png")
elif ext == "PDF":
    print("application/pdf")
elif ext == "TXT":
    print("text/plain")
elif ext == "ZIP":
    print("application/zip")
else:
    print("application/octet-stream")
