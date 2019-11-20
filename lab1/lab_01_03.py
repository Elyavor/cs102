'''
    Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m = ",m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m,pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")

code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space: ").split()
d, m, y = input("Enter three numbers splitted by \'.\': ").split('.')
print("{} + {} = {}".format(n1,n2,float(n1)+float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d,m,y,int(code)))
print("\n")

# 16
m = 10
pi = 3.1415927
print("m = %4d" % m)
print("pi = %.3f " % pi)
print("\n")

# 17
print("m = {}, pi = {}".format(m,pi))
print("\n")

# 18
year = input("Введите номер Вашего курса обучения: ")
print(year)

# 19
r1, m1, p1 = input("Введите значения Ваших баллов ЕГЭ по русскому языку, математике и профильному предмету соответсвенно, разделенных \',\': ").split(',')
print("Ваши баллы по русскому: %s , по математике: %s , по профильному предмету: %s" % (r1,m1,p1))
print("\n")

# 20
k = input("Введите 12-разрядное число в 12-ричной СС: ")
print("Исходное число: ", k)
print("Число в 10-тичной СС: ", int(k, 12))
print("\n")

# 21
e = int(input("Введите число: "))
print("Исходное число: ", e)
print("Умножение на 2: ", e<<1)
z = int(input("Введите число: "))
print("Исходное число: ", z)
print("Деление на 2:", z>>1)
print("\n")