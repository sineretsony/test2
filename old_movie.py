d = "Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, Psycho 1960"

list_now = d.split(",")
dictionary = {}

for i in list_now:
    temp = i.strip().rsplit(" ", 1)
    dictionary[temp[0]] = int(temp[1])

ol_mov = min(dictionary.items(), key=lambda x: x[1])[0]

print(dictionary)
print("Найстаріший фільм:", ol_mov)

