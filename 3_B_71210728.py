inp = input("Input : ")
a = len(inp)
print("Output : ")

for i in range(a):
    for j in range (a-i-1):
        print (" ",end = "")
    for j in range (i+1):
        print(inp[j], end = "")
    print()
for i in range(a):
    for e in range(i):
        print(" ", end= "" )
    for e in range(a-i):
        print(inp[e],end = "")
    print()

    