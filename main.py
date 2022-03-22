def say_hello ():
    print("Привет!",name,fam)
def say_hello1 ():
    print("Как твои дела?")
def say_hello2 ():
    print("Всё придёт,улыбайся. Никогда не сдавайся.")
def say_hello3 ():
    print("Где ты учишься или работаешь?")
def say_hello4 ():
    print("Пенсионер, иди растворись в воздухе.")
def say_hello5 ():
    print("С тобой даже поболтать не о чем ты еще слишком мал.")
def say_hello6 ():
    print("Ты молодец! Хорошего тебе дня, у тебя всё будет хорошо!")

name = input("Введите своё ИМЯ - ")
fam = input("Введите свою ФАМИЛИЮ - ")

say_hello()
say_hello1()
otvet = input("Введите хорошо или плохо - ")

if otvet == "хорошо":
    print("Это здорово у меня тоже всё хорошо!")
elif otvet == "плохо":
    print("Что случилось?")
    otvet_1 = input("Расскажи - ")
    say_hello2()
age = int(input("А сколько тебе лет? - "))
if age < 0:
    print("Введите реальный возраст вам не может быть меньше 1 года.")
elif age > 70:
    print("Я погляжу ты уже слишком стар для этого дерьма.")
    say_hello4()
elif age >= 20:
    print("Ооо да ты в самом соку.")
    say_hello3()
    otvet_2 = input("Расскажи немного о себе - ")
    say_hello6()
elif age <= 20:
    print("Ты ещё молодой, иди учи уроки.")
    say_hello5()