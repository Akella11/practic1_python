# Запитуємо у користувача чотири числа
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# Обчислюємо суми і ділимо їх
sum1 = num1 + num2
sum2 = num3 + num4
result = sum1 / sum2

# Виводимо результат з двома цифрами після коми
print(f"Result: {result:.2f}")
