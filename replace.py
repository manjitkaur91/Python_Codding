search_text="key"
Replace_text="join"
with open('file.txt','r') as file:
     data = file.read()
     data=data.replace(search_text,Replace_text)
     with open('file.txt','w') as file:
        file.write(data)
        print("replaced text")