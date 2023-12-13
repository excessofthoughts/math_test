from random import *

def generating():
    symbol = choice(['*', '/', '+', '-'])
    a = randint(1, 25)
    b = randint(1, 25)
    itg = f'{a}{symbol}{b}'
    return itg
def check(itg, ans):
    try:
        ans = float(ans)
        eee = eval(itg)
        return round(ans, 2) == round(eee, 2)
    except ValueError:
        return False
def work(number=5):
    right = 0
    for _ in range(number):
        itg = generating()
        ans = input(f'{itg}=')
        if check(itg, ans):
            right += 1
        else:
            print(round(eval(itg), 2))
    mark = right/number * 100
    print(mark, '%')
    if mark >= 85:
        print('все чудесно! 5!')
    elif mark >= 60:
        print('нууу, это 4!')
    elif mark >= 30:
        print('бывает, 3!')
    else:
        print('2, учить математику надо!')

print('Всем здрасте! Добро пожаловать в игру!')
level = int(input('Сколько вопросов?'))
if level >= 4:
    print("отлично, поехали")
    work(level)
else:
    print("Маловато, решай 5")
    work()