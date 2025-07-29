# Determine the MIME type of a file based on its extension

file_name = input("File name: ")
file_name = file_name.lower().strip()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

    
#option 2
'''
file_name = input("File name: ")
file_name = file_name.lower().strip()

match file_name:
    case file_name if file_name.endswith(".gif"):
        print("image/gif")
    case file_name if file_name.endswith(".jpg") | file_name.endswith(".jpeg"):
        print("image/jpeg")
    case file_name if file_name.endswith(".png"):
        print("image/png")
    case file_name if file_name.endswith(".pdf"):
        print("application/pdf")
    case file_name if file_name.endswith(".txt"):
        print("text/plain")
    case file_name if file_name.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")
 '''       
 '''       
#option 3 using functions
def get_mime_type():
    file_name = input("File name: ")
    file_name = file_name.lower().strip()

    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"
    
results = get_mime_type()  # calling the function to execute it
print(results)  # printing the result returned by the function
'''