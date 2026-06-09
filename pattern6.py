open("pattern6.txt","w").write(" ")

for i in range(4):
    for j in range(4):
        print("#",end=" ")
        open("pattern6.txt","a").write("# ")
    print() 
    open("pattern6.txt","a").write("\n")   