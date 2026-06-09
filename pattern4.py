open("pattern4.txt","w").write(" ")

for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
        open("pattern4.txt","a").write("* ")
    print()
    open("pattern4.txt","a").write("\n")    