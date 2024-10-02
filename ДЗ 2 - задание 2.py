repeat = int(input('Сколько раз повторим? '))
#пытался сделать цикл, но получилось только через костыли
x = 0
while repeat > x:
    print(x)
    x += 1
    ticket = [int(i) for i in input('Номер вашего билетика? ')]
    if sum(ticket[:3]) == sum(ticket[3:]):
        print('Тебе повезло!')
    else:
        print('Повезет в следующий раз...')