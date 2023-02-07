word = input("Введіть будь ласка слово: ")
num_l = len(word)
par = num_l // 2
rem = num_l % 2
if rem == 0:
    l1 = par + 1
    rem = par - 1
    print("Ваше слово парне, дві літери із середини: ", word[rem:l1])
elif rem > 0:
    print("Ваше слово не парне, літера в центрі: ", word[par])
