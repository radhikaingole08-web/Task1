open("pattern1.txt","w").write(" ")
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")  
        open("pattern1.txt","a").write("* ")
    print()
    open("pattern1.txt","a").write("\n")