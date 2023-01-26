import random
t = random.randint(1, 3)
f = random.randint(1, 4)
def Gadalka():
    choose = random.randint(1, 7)
    if (choose == 1): print("Дыа")
    elif (choose == 2): print("Нит")
    elif (choose == 3): print("Звёзды говорят да")
    elif (choose == 4): print("Звезды говорят нет")
    elif (choose == 5): print("Шар нинает")
    elif (choose == 6): print("Шар молчит")
    elif (choose == 7): print("Я нинаю")

def Voprosi():
    t = random.randint(1, 3)
    if (t == 1):
        print("Спроси шар, мой друг")
    elif (t == 2):
        print("Задайте интересующий вас вопрос")
    elif (t == 3):
        print("Задай свой вопрос")




while True:
    Voprosi()
    govorit = input()
    if (govorit == "выход"):
        break
    print('---------------------------------------------------------------')
    if (f == 1) :
        Voprosi()
        print("_/(@)\_")
        Gadalka()
    elif (f == 2):
        Voprosi()
        print("_/(&)\_")
        Gadalka()
    elif (f == 3):
        Voprosi()
        print("_/(%)\_")
        Gadalka()
    elif (f == 4):
        Voprosi()
        print("_/(*)\_")
        Gadalka()
    print('---------------------------------------------------------------')
