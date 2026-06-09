open("pattern3.txt","w").write("")
num=1
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        open("pattern3.txt","a").write(str(num) + " ")
        num+=1
    print()
    open("pattern3.txt","a").write("\n")    