import math
print("Список команд: Сложение, Вычитание, Умножение, Деление, Окр. в меньшую, Окр. в большую, Логарифм, Выход.")
while True:
        print("Выберите действие:")
        f=input()
        if f=='Сложение' or f=='сложение':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print("Введите число:")
                                b=input()
                                if b.isnumeric():
                                        print(int(a)+int(b))
                                        break
                                else:
                                        print('Неверный ввод.')
                        else: print("Неверный ввод.")
        elif f=='Вычитание' or f=='вычитание':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print("Введите число:")
                                b=input()
                                if b.isnumeric():
                                        print(int(a)+int(b))
                                        break
                                else:
                                        print("Неверный ввод.")
                        else: print("Неверный ввод.")
        elif f=='Список команд' or f=='список команд':
                print("Список команд: Сложение, Вычитание, Умножение, Деление, Окр. в меньшую, Окр. в большую, Логарифм, Выход.")
        elif f=="Выход" or f=='выход':
                break
        elif f=='Умножение' or f=='умножение':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print("Введите число:")
                                b=input()
                                if b.isnumeric():
                                        print(int(a)*int(b))
                                        break
                                else:
                                        print("Неверный ввод.")
        elif f=='Деление' or f=='деление':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print("Введите число:")
                                b=input()
                                if b.isnumeric():
                                        print(int(a)/int(b))
                                        break
                                else:
                                        print("Неверный ввод.")
                        else: print("Неверный ввод.")
        elif f=='Окр. в меньшую' or f=='окр. в меньшую':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print(math.floor(int(a)))
                                break
                        else: print("Неверный ввод.")
        elif f=='Окр. в большую' or f=='окр. в большую':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print(math.ceil(int(a)))
                                break
                        else: print("Неверный ввод.")
        elif f=='Логарифм' or f=='логарифм':
                print("Введите число:")
                while True:
                        a=input()
                        if a.isnumeric():
                                print("Введите основание:")
                                b=input()
                                if b.isnumeric():
                                        print(math.log(int(a),int(b)))
                                        break
                                else:
                                        print("Неверный ввод.")
                        else: print("Неверный ввод.")
