I= int(input("Input : "))
print("Output : ")

for a in range(I):
    for b in range(I-a-1):
        print(" ",end = "  ")
    for b in range(I):
        if b == 0 or a == I-1 or a == b:
            print("*", end = "  ")
        else:
            print(end = "   ")
    print()




