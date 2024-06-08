# Надаємо змінним значення
a = 5
b = 10

# Логічні вирази з оператором and
print((a < b) and (b > 15))  # False
print((a < b) and (b == 10))  # True

# Логічні вирази з оператором or
print((a > b) or (b < 20))  # True
print((a == 5) or (b < 5))  # True

# Логічні вирази з рядковими змінними
str1 = "hello"
str2 = ""
print(bool(str1) and bool(str2))  # False
print(bool(str1) or bool(str2))  # True

# Програма для порівняння чисел
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1 > num2)
