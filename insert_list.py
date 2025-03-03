if __name__ == '__main__':

    N = int(input("Enter value "))
    lst=[]
    for _ in range(N):
        command=input().split()
        if command[0]=="insert":
            lst.insert(int(command[1]),int(command[2]))
        elif command[0]=="print":
            print(lst)