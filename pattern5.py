open("pattern5.txt","w").write(" ")

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
        open("pattern5.txt","a").write(str(j) + " ")
    print()
    open("pattern5.txt","a").write("\n")    