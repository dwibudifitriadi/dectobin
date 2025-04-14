def dectobin(n):
    q = []
    b = []
    q.append(n // 2)
    print("Q[0] = INT ("+str(n)+" // 2) = "+str(n//2))
    b.append(n - 2 * q[0])
    print("B[0] = "+str(n) +" - 2 * "+str(q[0])+" = "+str(n - 2 * q[0]))
    j = 0
    while q[j]!= 0:
        j += 1
        q.append(q[j-1] // 2)
        print("Q["+str(j)+"] = INT ("+str(q[j-1])+"/2) = "+str(q[j+1 // 2]))
        b.append(q[j-1] - 2 * q[j])
        print("B["+str(j)+"] = Q ["+str(q[j-1])+" - 2 * "+str(q[j])+"] = "+str(q[j-1] - 2 * q[j]))
    string_kosong = ''
    for i in range(len(b) - 1, -1, -1):
        string_kosong += str(b[i])
    return string_kosong
n = int(-1)
while n < 0:
    n = int(input("Masukkan Bilangan Desimal :"))
print(f"Bilangan biner: {dectobin(n)}")
