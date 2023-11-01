try:
    print("Початок коду")
    print(10/0)
    print("Немає помилок")
except (NameError, ZeroDivisionError) as error:
    print(error)
else:
    print("else")
finally:
    print("Код, який буде виведено в будь-якому випабку")

print("Код після капсули")