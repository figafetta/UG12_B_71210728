n = int(input("Masukkan banyak bilangan : "))
t = 1
print("Total = ", end = "")

for i in range(1,n+1):
    if i%3==0:
        t = t + (i * -1)
        print("- ", str(i), end = " ")
    elif i%7==0:
        t = t + 0
        print("+ 0", end = " ")
    elif i==1:
        print(str(i), end = " ")
    else:
        t = t + i
        print("+ ", str(i), end = " ")

print("\nHasil perhitungan diatas ialah " + str(t))