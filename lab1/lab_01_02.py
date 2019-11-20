'''
   Логические операции
'''
f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n\n")

'''
    Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j)))
print("k = %d; k in binary format: %s" % (k, bin(k)))
print("j & k: %d; binary: %s" % (j & k, bin(j & k)))
# побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k)))
# побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k)))
# побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k))) 
# инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k>>1, bin(k>>1))) 
# сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k<<1, bin(k<<1))) 
# сдвиг на один бит влево
print("\n\n")

# 10, 11
A = 77
B = 33
C = True
D = False
print("C: ", C)
print("D: ", D)
print("not (C and D): ", not (C and D))
print("C and D or not (C and D): ", C and D or not (C and D))
print("not C or D: ", not C or D)
print("\n")
print("A = ", A)
print("B = ", B)
print("A <= B: ", A <= B)
print("A > B or A == B: ", A > B or A == B)
print("not (A < B): ", not (A < B))
print("\n")

# 12
s = 154
p = 6
print("s = ", s,"; s in binary format: ", bin(s))
print("p = ", p,"; p in binary format: ", bin(p))
print("\n")

# 13
s = s | p
print("s = s | p: " , s, "; binary: " , bin(s))
print("\n")

# 14
s = s>>2
print("s>>2: ", s, "; binary: " , bin(s))
p = p>>2
print("p>>2: ", p, "; binary: " , bin(p))
print("\n")