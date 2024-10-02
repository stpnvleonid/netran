repeat = int(input('Сколько раз повторим? '))
#пытался сделать цикл, но получилось только через костыли
x = 0
while repeat > x:
    print(x)
    x += 1
    word = input("Введите слово: ")
    f_Str = len(word)
    g_Str = f_Str / 2
    if f_Str % 2 != 0:
        print(word[int(g_Str)])
    else:
        print(word[int(g_Str)-1:int(g_Str)+1])