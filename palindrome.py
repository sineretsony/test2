pal_input = input("Введіть слово на перевірку паліндрому: ")

pal_strip = pal_input.strip()
pal_lower = pal_strip.lower()
pal_mirror = pal_lower[::-1]

if pal_mirror.count(pal_lower):
    print(f"Ваше слово '{pal_input}' — паліндром, вітання!")
else:
    print(f"Слово '{pal_input}' не є паліндромом, спробуйте ще")
