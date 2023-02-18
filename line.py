word = input("Введіть будь ласка слово: ")

num_l = len(word)
par = num_l // 2
rem = num_l % 2

if rem == 0:
    len_num = par + 1
    rem = par - 1
    print("Ваше слово парне, дві літери із середини: ", word[rem:len_num])
elif rem > 0:
    print("Ваше слово непарне, літера в центрі: ", word[par])
