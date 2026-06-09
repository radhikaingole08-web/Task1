open("pattern2.txt","w").write(" ")
for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
        open("pattern2.txt","a").write(str(i) + " ")
    print() 
    open("pattern2.txt","a").write("\n")   