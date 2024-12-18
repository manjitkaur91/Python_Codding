with open ('file.txt', 'r') as file :
    content=file.read()
    if 'key' in content:
        print("exist")
    else:
         print("not")
